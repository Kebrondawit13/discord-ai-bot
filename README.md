Markdown# Gemini Discord AI Bot

A Discord AI bot powered by Google's Gemini API with personality modes, vision capabilities, and memory.

## Features

- **Gemini-Powered Conversations:** Advanced AI responses in server channels and direct messages.
- **Personality Modes:** 
  - `!mode` - Normal Mode
  - `!mean` - Mean Mode
  - `!kind` - Kind Mode
- **No Mention Needed:** Engages naturally in designated channels.
- **Vision Support:** Image and GIF analysis via Gemini.
- **Context Memory:** Remembers recent conversation history per user.
- **Built-in Guardrails:** Per-user cooldowns and Gemini API rate-limit handling.

---

## Prerequisites

- Chromebook with ChromeOS Linux development environment enabled
- Python 3.12+
- Git and pip
- Discord Account & Developer Application
- Gemini API Key

---

## Chromebook Linux Setup

Follow these steps in order.

### 1. Enable Linux Environment

1. On your Chromebook, go to **Settings → Advanced → Developers → Linux development environment**.
2. Turn **Linux** on.
3. Open the **Terminal** app from your app drawer.

### 2. Install Python and Git

Run the following command in your terminal:

```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv git -y
Verify the installations:Bashpython3 --version
git --version
3. Download the BotClone the repository and enter the directory:Bashgit clone [https://github.com/Kebrondawit13/discord-ai-bot.git](https://github.com/Kebrondawit13/discord-ai-bot.git)
cd discord-ai-bot
4. Set Up Python Virtual EnvironmentCreate and activate the environment:Bashpython3 -m venv venv
source venv/bin/activate
(You should now see (venv) at the start of your terminal prompt).5. Install DependenciesInstall all required Python packages at once:Bashpython -m pip install -r requirements.txt
API & Bot Setup6. Create Your Discord BotGo to the Discord Developer Portal.Click New Application and set a name.Navigate to Bot → Add Bot.Click Reset Token and copy your Bot Token. (Keep this token private!)7. Enable Gateway IntentsIn the Developer Portal under Bot → Privileged Gateway Intents, enable:Message Content IntentServer Members IntentClick Save Changes.8. Invite the Bot to Your ServerGo to OAuth2 → URL Generator.Select the bot scope.Under Bot Permissions, select:View ChannelsSend MessagesRead Message HistoryEmbed LinksAttach FilesCopy the generated URL at the bottom, paste it into your browser, and select your server.9. Get a Gemini API KeyGo to Google AI Studio.Click Create API Key.Copy your API key.Configuration & Launch10. Create the .env FileInside the discord-ai-bot folder, open the nano editor:Bashnano .env
Paste the following and replace the placeholder text with your actual keys:Code snippetDISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
Save and exit:Press CTRL + O, then Enter (Save)Press CTRL + X (Exit)Note: Never commit or upload your .env file to GitHub.11. Run the BotTo start the bot anytime:Bashcd ~/discord-ai-bot
source venv/bin/activate
python ai.py
Keep the terminal window open while running. Press CTRL + C to stop the bot.Usage & CommandsUse the ! prefix to trigger commands in Discord:CommandModeDescription!modeNormal ModeStandard, helpful Gemini interactions!meanMean ModeSarcastic and witty responses!kindKind ModeWarm and overly encouraging responsesNote: Slash commands (e.g., /mode) are not supported.Updating the BotTo pull the latest updates from GitHub:Bashcd ~/discord-ai-bot
source venv/bin/activate
git pull
python -m pip install -r requirements.txt
python ai.py
TroubleshootingBot fails to start: Ensure venv is activated (source venv/bin/activate) and your .env file is in the root directory.Bot is online but doesn't reply:Verify Message Content Intent is enabled in the Developer Portal.Confirm the bot has read/write permissions in that channel.Ensure your API keys in .env are accurate without extra spaces.
