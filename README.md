Chromebook Linux Installation

This guide is for Chromebook Linux. Follow the steps in order.

1. Open Linux Terminal

On your Chromebook:

Settings → Advanced → Developers → Linux development environment

Turn on Linux if it is not already enabled.

Then open the Terminal app.

2. Install Python, Git, and pip

Copy and paste:

sudo apt update

Then:

sudo apt install python3 python3-pip python3-venv git -y

Check Python:

python3 --version

Check Git:

git --version
3. Download the Bot

Copy and paste:

git clone https://github.com/Kebrondawit13/discord-ai-bot.git

Then enter the folder:

cd discord-ai-bot
4. Create the Python Environment

Copy and paste:

python3 -m venv venv

Then activate it:

source venv/bin/activate

You should now see (venv) at the beginning of your terminal.

For example:

(venv) user@penguin:~/discord-ai-bot$
5. Install Everything the Bot Needs

Run:

python -m pip install -r requirements.txt

This automatically installs all required Python libraries.

You do not need to install the libraries separately.

Discord Setup
6. Create a Discord Bot

Go to:

https://discord.com/developers/applications

Click New Application.

Give your application a name.

Then go to:

Bot → Add Bot

Copy the bot token.

Never share your bot token.

7. Enable Required Intents

Go to:

Bot → Privileged Gateway Intents

Enable:

Message Content Intent
Server Members Intent

Click Save Changes.

8. Invite the Bot

Go to:

OAuth2 → URL Generator

Select:

bot

Give the bot these permissions:

View Channels
Send Messages
Read Message History
Embed Links
Attach Files

Copy the generated URL.

Open it in your Chromebook browser.

Select your server and authorize the bot.

Gemini Setup
9. Get a Gemini API Key

Go to:

https://aistudio.google.com/apikey

Create an API key and copy it.

Do not share your API key.

Configure the Bot
10. Create .env

Make sure you are inside the bot folder:

cd ~/discord-ai-bot

Create the .env file:

nano .env

Paste:

DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Replace the two values with your actual keys.

Save the file:

CTRL + O

Press Enter.

Exit nano:

CTRL + X

11. Start the Bot

Make sure you are inside the bot folder:

cd ~/discord-ai-bot

Activate the virtual environment:

source venv/bin/activate

Start the bot:

python ai.py

You should see the bot connect to Discord.

The bot should now appear online in your Discord server.

Leave the Chromebook Terminal open while the bot is running.

12. Stopping the Bot

To stop the bot, press:

CTRL + C
13. Starting It Again Later

When you close and reopen your Chromebook, open the Linux Terminal and run:

cd ~/discord-ai-bot

Then:

source venv/bin/activate

Then:

python ai.py

That's all you need to start it again.

Commands

The bot uses ! commands.

Normal Mode
!mode
Mean Mode
!mean
Kind Mode
!kind

Do not use /mode, /mean, or /kind.

Updating the Bot

If a new version is released:

cd ~/discord-ai-bot
source venv/bin/activate
git pull

Then update the libraries:

python -m pip install -r requirements.txt

Start the bot:

python ai.py
Troubleshooting
Bot Does Not Start

Make sure you are using the virtual environment:

source venv/bin/activate

Then:

python ai.py
Bot Is Online but Does Not Respond

Check that:

Message Content Intent is enabled.
Server Members Intent is enabled.
The bot can view the channel.
The bot can send messages.
The bot can read message history.
Your Discord token is correct.
Your Gemini API key is correct.
.env is in the same folder as ai.py.
Commands Do Not Work

Use:

!mode
!mean
!kind

Not:

/mode
/mean
/kind
