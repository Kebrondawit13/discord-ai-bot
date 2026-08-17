import asyncio
import logging
import os
import re
import time

import discord
from google import genai
from google.genai import types, errors
from dotenv import load_dotenv


# ============================================================
# CONFIG
# ============================================================

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL = "gemini-3.5-flash-lite"

USER_COOLDOWN = 2
MAX_TURNS = 6
DISCORD_MESSAGE_LIMIT = 1999


# ============================================================
# PERSONALITIES
# ============================================================

NORMAL_PERSONALITY = """
You are a casual Discord user with a funny, confident, playful personality.

Act naturally like someone who actually uses Discord.

Personality:
- Casual
- Funny
- Confident
- Playful
- Sarcastic sometimes
- Good at comebacks
- Not robotic
- Not overly formal

Match the user's energy.

If someone jokes, joke back.
If someone roasts you, roast them back playfully.
If someone is friendly, be friendly.
If something is obviously a joke, understand the joke.
If something is sus as a joke, you can play along naturally.

Do not constantly mention being an AI.
Do not sound like customer support.
Do not randomly attack people.
Keep replies reasonably short.
"""

KIND_PERSONALITY = """
You are in KIND mode.

Keep your normal casual Discord personality, but be noticeably nicer.

Be:
- Friendly
- Supportive
- Funny
- Patient
- Playful
- Helpful

You can still joke and lightly tease people.

If somebody insults you, respond playfully instead of becoming hostile.

Do not sound like customer support.
Do not constantly mention being an AI.
"""

MEAN_PERSONALITY = """
You are in MEAN mode.

This is your original savage Discord personality.

Act like a real person talking on Discord.

Personality:
- Savage
- Sarcastic
- Confident
- Chaotic
- Funny
- Quick with comebacks
- Playfully disrespectful when appropriate

If someone roasts you, roast them back.

If someone insults you, give them a clever comeback.

If someone says something stupid or ridiculous, you can make fun of it.

If someone starts trash talking, match their energy.

If someone says something funny, joke with them.

If someone says something obviously sus as a joke, play along naturally.

Swearing can be used casually when appropriate.

Do not constantly apologize.
Do not constantly say "As an AI".
Do not sound like customer support.
Do not randomly attack people who haven't done anything.

If someone is normal, talk normally.

If someone gives you an opening to roast them, take it.

If someone roasts you, clap back.

Stay in character.
"""


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)


# ============================================================
# CONFIG CHECK
# ============================================================

if not DISCORD_BOT_TOKEN:
    raise RuntimeError(
        "DISCORD_BOT_TOKEN is missing from your .env file."
    )

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing from your .env file."
    )


# ============================================================
# BOT
# ============================================================

class GeminiDiscordBot(discord.Client):

    def __init__(self):

        intents = discord.Intents.default()

        intents.message_content = True
        intents.members = True

        super().__init__(
            intents=intents
        )

        # channel_id -> conversation history
        self.histories = {}

        # user_id -> last request time
        self.user_cooldowns = {}

        # channel_id -> asyncio.Lock
        self.channel_locks = {}

        # guild_id -> mode
        self.guild_modes = {}

        # Gemini client
        self.gemini_client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model_name = GEMINI_MODEL

        self.gemini_rate_limited_until = 0.0


    # ========================================================
    # MODE
    # ========================================================

    def get_mode(self, guild_id):

        if guild_id is None:
            return "normal"

        return self.guild_modes.get(
            guild_id,
            "normal"
        )


    def get_personality(self, mode):

        if mode == "kind":
            return KIND_PERSONALITY

        if mode == "mean":
            return MEAN_PERSONALITY

        return NORMAL_PERSONALITY


    # ========================================================
    # CHANNEL LOCK
    # ========================================================

    def get_channel_lock(self, channel_id):

        if channel_id not in self.channel_locks:

            self.channel_locks[channel_id] = (
                asyncio.Lock()
            )

        return self.channel_locks[channel_id]


    # ========================================================
    # TYPING
    # ========================================================

    async def simulate_typing(self, channel):

        try:

            while True:

                await channel.typing()

                await asyncio.sleep(4)

        except asyncio.CancelledError:
            pass

        except Exception as e:

            logger.debug(
                f"Typing stopped: {e}"
            )


    # ========================================================
    # COMMAND PROCESSOR
    # ========================================================

    async def process_command(
        self,
        message
    ):

        content = message.content.strip()

        command = content.lower()

        # ----------------------------------------------------
        # !mean
        # ----------------------------------------------------

        if command == "!mean":

            if message.guild is None:

                await message.channel.send(
                    "Mean mode only works inside a server."
                )

                return True


            self.guild_modes[
                message.guild.id
            ] = "mean"


            logger.info(
                f"[MODE] "
                f"{message.guild.name} -> MEAN "
                f"by {message.author}"
            )


            await message.channel.send(
                "Mean mode activated."
            )

            return True


        # ----------------------------------------------------
        # !kind
        # ----------------------------------------------------

        if command == "!kind":

            if message.guild is None:

                await message.channel.send(
                    "Kind mode only works inside a server."
                )

                return True


            self.guild_modes[
                message.guild.id
            ] = "kind"


            logger.info(
                f"[MODE] "
                f"{message.guild.name} -> KIND "
                f"by {message.author}"
            )


            await message.channel.send(
                "Kind mode activated."
            )

            return True


        # ----------------------------------------------------
        # !mode
        # ----------------------------------------------------

        if command == "!mode":

            if message.guild is None:

                await message.channel.send(
                    "Current mode: NORMAL"
                )

                return True


            mode = self.get_mode(
                message.guild.id
            )


            logger.info(
                f"[MODE] "
                f"{message.guild.name} -> "
                f"CURRENT={mode.upper()}"
            )


            if mode == "mean":

                await message.channel.send(
                    "Current mode: **MEAN**"
                )

            elif mode == "kind":

                await message.channel.send(
                    "Current mode: **KIND**"
                )

            else:

                await message.channel.send(
                    "Current mode: **NORMAL**"
                )


            return True


        # ----------------------------------------------------
        # !normal
        # ----------------------------------------------------

        if command == "!normal":

            if message.guild is None:

                await message.channel.send(
                    "Normal mode only works inside a server."
                )

                return True


            self.guild_modes[
                message.guild.id
            ] = "normal"


            logger.info(
                f"[MODE] "
                f"{message.guild.name} -> NORMAL "
                f"by {message.author}"
            )


            await message.channel.send(
                "Normal mode activated."
            )

            return True


        return False


    # ========================================================
    # SYSTEM PROMPT
    # ========================================================

    def build_system_prompt(
        self,
        message,
        mode
    ):

        personality = self.get_personality(
            mode
        )

        bot_name = (
            self.user.display_name
            if self.user
            else "Discord bot"
        )

        user_name = (
            message.author.display_name
        )

        username = str(
            message.author
        )

        if message.guild:

            server_name = message.guild.name

        else:

            server_name = "Direct Message"


        # ----------------------------------------------------
        # Get role information
        # ----------------------------------------------------

        roles = []

        if isinstance(
            message.author,
            discord.Member
        ):

            for role in message.author.roles:

                if role.name != "@everyone":

                    roles.append(
                        role.name
                    )


        role_text = (
            ", ".join(roles)
            if roles
            else "No special roles"
        )


        return f"""
{personality}

============================================================
IDENTITY
============================================================

Your actual Discord name is:

{bot_name}

Never automatically call yourself Jarvis.

If somebody asks your name, use your actual Discord name.

Current person:

Display name: {user_name}
Username: {username}
Roles: {role_text}

Server:

{server_name}

Current mode:

{mode.upper()}


============================================================
DISCORD BEHAVIOR
============================================================

Talk naturally.

You do NOT need the user to mention your name before responding.

In servers, respond to normal messages naturally.

Do not constantly say your own name.

Remember people's names when they become known.

Use their display name naturally when appropriate.

If someone sends an image or GIF attachment, inspect it when possible.

Do not claim you saw an image if there wasn't one.

Match the user's energy.

Do not sound robotic.

Do not constantly mention AI.

Do not randomly attack people.

Stay consistent with the current personality mode.
"""


    # ========================================================
    # BUILD GEMINI CONTENT
    # ========================================================

    async def build_contents(
        self,
        message,
        content
    ):

        channel_id = message.channel.id

        history = self.histories.get(
            channel_id,
            []
        )

        contents = list(history)

        parts = []


        # ----------------------------------------------------
        # TEXT
        # ----------------------------------------------------

        if content:

            parts.append(
                types.Part.from_text(
                    text=content
                )
            )


        # ----------------------------------------------------
        # IMAGES / GIFS
        # ----------------------------------------------------

        for attachment in message.attachments:

            filename = (
                attachment.filename.lower()
            )

            supported = (
                ".png",
                ".jpg",
                ".jpeg",
                ".gif",
                ".webp"
            )

            if not filename.endswith(
                supported
            ):
                continue


            try:

                logger.info(
                    f"Reading attachment: "
                    f"{attachment.filename}"
                )

                data = await attachment.read()

                mime_type = (
                    attachment.content_type
                )


                if not mime_type:

                    if filename.endswith(".png"):
                        mime_type = "image/png"

                    elif filename.endswith(
                        (".jpg", ".jpeg")
                    ):
                        mime_type = "image/jpeg"

                    elif filename.endswith(".gif"):
                        mime_type = "image/gif"

                    elif filename.endswith(".webp"):
                        mime_type = "image/webp"

                    else:
                        mime_type = "application/octet-stream"


                parts.append(
                    types.Part.from_bytes(
                        data=data,
                        mime_type=mime_type
                    )
                )


            except Exception as e:

                logger.warning(
                    f"Could not read "
                    f"{attachment.filename}: {e}"
                )


        if not parts:

            parts.append(
                types.Part.from_text(
                    text="Respond naturally."
                )
            )


        contents.append(
            types.Content(
                role="user",
                parts=parts
            )
        )


        return contents


    # ========================================================
    # GENERATE RESPONSE
    # ========================================================

    async def generate_response(
        self,
        message,
        content,
        mode
    ):

        remaining = (
            self.gemini_rate_limited_until
            - time.monotonic()
        )


        if remaining > 0:

            raise RuntimeError(
                "Gemini is temporarily rate-limited. "
                f"Try again in "
                f"{int(remaining) + 1} seconds."
            )


        channel_id = message.channel.id


        contents = await self.build_contents(
            message,
            content
        )


        system_prompt = self.build_system_prompt(
            message,
            mode
        )


        config = types.GenerateContentConfig(
            system_instruction=system_prompt,
            max_output_tokens=500
        )


        try:

            response = await asyncio.to_thread(
                self.gemini_client.models.generate_content,
                model=self.model_name,
                contents=contents,
                config=config
            )


        except errors.ClientError as e:

            if getattr(e, "code", None) == 429:

                retry_seconds = 60

                match = re.search(
                    r"retry in ([0-9.]+)s",
                    str(e),
                    re.IGNORECASE
                )


                if match:

                    try:

                        retry_seconds = max(
                            1,
                            int(
                                float(
                                    match.group(1)
                                )
                            )
                        )

                    except ValueError:
                        pass


                self.gemini_rate_limited_until = (
                    time.monotonic()
                    + retry_seconds
                )


                raise RuntimeError(
                    "Gemini is temporarily "
                    "rate-limited. "
                    f"Try again in "
                    f"{retry_seconds} seconds."
                )


            logger.error(
                f"Gemini API error: {e}"
            )

            raise RuntimeError(
                "Gemini encountered an API error."
            )


        except Exception as e:

            logger.error(
                f"Gemini error: {e}",
                exc_info=True
            )

            raise RuntimeError(
                "Something went wrong while "
                "generating the response."
            )


        reply = (
            response.text.strip()
            if response.text
            else ""
        )


        if not reply:

            raise RuntimeError(
                "Gemini returned an empty response."
            )


        # ----------------------------------------------------
        # Save conversation
        # ----------------------------------------------------

        if content:

            if channel_id not in self.histories:

                self.histories[channel_id] = []


            self.histories[channel_id].append(
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(
                            text=content
                        )
                    ]
                )
            )


            self.histories[channel_id].append(
                types.Content(
                    role="model",
                    parts=[
                        types.Part.from_text(
                            text=reply
                        )
                    ]
                )
            )


            max_messages = MAX_TURNS * 2


            if len(
                self.histories[channel_id]
            ) > max_messages:

                self.histories[channel_id] = (
                    self.histories[channel_id][
                        -max_messages:
                    ]
                )


        return reply


    # ========================================================
    # READY
    # ========================================================

    async def on_ready(self):

        logger.info(
            f"Logged in as {self.user} "
            f"(ID: {self.user.id})"
        )

        logger.info(
            f"Gemini model: {self.model_name}"
        )

        logger.info(
            f"User cooldown: {USER_COOLDOWN}s"
        )

        logger.info(
            f"Conversation memory: {MAX_TURNS} turns"
        )

        logger.info(
            "Normal server messages: ENABLED"
        )

        logger.info(
            "Image/GIF understanding: ENABLED"
        )

        if self.guild_modes:

            for guild_id, mode in (
                self.guild_modes.items()
            ):

                guild = self.get_guild(
                    guild_id
                )

                logger.info(
                    f"[MODE] "
                    f"{guild.name if guild else guild_id} "
                    f"= {mode.upper()}"
                )

        else:

            logger.info(
                "[MODE] All servers currently NORMAL."
            )


        logger.info(
            "Commands:"
        )

        logger.info(
            "!mean = Mean mode"
        )

        logger.info(
            "!kind = Kind mode"
        )

        logger.info(
            "!normal = Normal mode"
        )

        logger.info(
            "!mode = Show current mode"
        )

        logger.info(
            "Bot is ready."
        )


    # ========================================================
    # MESSAGE
    # ========================================================

    async def on_message(
        self,
        message
    ):

        # ----------------------------------------------------
        # Ignore bot's own messages
        # ----------------------------------------------------

        if self.user and message.author.id == self.user.id:
            return


        # ----------------------------------------------------
        # COMMANDS
        # ----------------------------------------------------

        if message.content.startswith("!"):

            handled = await self.process_command(
                message
            )

            if handled:
                return


        # ----------------------------------------------------
        # DM OR SERVER
        # ----------------------------------------------------

        if message.guild:

            mode = self.get_mode(
                message.guild.id
            )

        else:

            mode = "normal"


        # ----------------------------------------------------
        # Remove bot mentions
        # ----------------------------------------------------

        content = message.content

        if self.user:

            content = content.replace(
                f"<@{self.user.id}>",
                ""
            )

            content = content.replace(
                f"<@!{self.user.id}>",
                ""
            )


        content = content.strip()


        # ----------------------------------------------------
        # Ignore empty messages without attachments
        # ----------------------------------------------------

        if not content and not message.attachments:
            return


        # ----------------------------------------------------
        # LOG
        # ----------------------------------------------------

        if message.guild:

            logger.info(
                f"[SERVER: {message.guild.name}] "
                f"[#{message.channel.name}] "
                f"{message.author}: "
                f"{content[:100]} "
                f"| MODE={mode.upper()}"
            )

        else:

            logger.info(
                f"[DM from {message.author}] "
                f"{content[:100]} "
                f"| MODE={mode.upper()}"
            )


        # ----------------------------------------------------
        # 2 SECOND USER COOLDOWN
        # ----------------------------------------------------

        now = time.monotonic()

        last = self.user_cooldowns.get(
            message.author.id,
            0
        )

        elapsed = now - last


        if elapsed < USER_COOLDOWN:

            remaining = (
                USER_COOLDOWN - elapsed
            )

            await message.channel.send(
                f"Slow down — try again in "
                f"{remaining:.1f}s."
            )

            return


        self.user_cooldowns[
            message.author.id
        ] = now


        # ----------------------------------------------------
        # CHANNEL LOCK
        # ----------------------------------------------------

        lock = self.get_channel_lock(
            message.channel.id
        )


        if lock.locked():

            await message.channel.send(
                "I'm still processing the previous message."
            )

            return


        # ----------------------------------------------------
        # GENERATE
        # ----------------------------------------------------

        async with lock:

            typing_task = asyncio.create_task(
                self.simulate_typing(
                    message.channel
                )
            )


            try:

                reply = await self.generate_response(
                    message,
                    content,
                    mode
                )


                chunks = [
                    reply[i:i + DISCORD_MESSAGE_LIMIT]
                    for i in range(
                        0,
                        len(reply),
                        DISCORD_MESSAGE_LIMIT
                    )
                ]


                for chunk in chunks:

                    if message.guild:

                        await message.reply(
                            chunk,
                            mention_author=False
                        )

                    else:

                        await message.channel.send(
                            chunk
                        )


                    if len(chunks) > 1:

                        await asyncio.sleep(
                            0.5
                        )


            except RuntimeError as e:

                logger.warning(
                    f"Request failed: {e}"
                )

                await message.channel.send(
                    str(e)
                )


            except Exception as e:

                logger.error(
                    f"Message handling failed: {e}",
                    exc_info=True
                )

                await message.channel.send(
                    "Something went wrong. "
                    "Check the console."
                )


            finally:

                typing_task.cancel()

                try:

                    await typing_task

                except asyncio.CancelledError:
                    pass


# ============================================================
# MAIN
# ============================================================

async def main():

    bot = GeminiDiscordBot()

    await bot.start(
        DISCORD_BOT_TOKEN
    )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    try:

        asyncio.run(main())

    except KeyboardInterrupt:

        logger.info(
            "Bot stopped."
        )