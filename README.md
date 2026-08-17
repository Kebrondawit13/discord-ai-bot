# Gemini Discord AI Bot

A Discord AI bot powered by Google's Gemini API.

## Features

- Gemini-powered conversations
- Casual Discord-style personality
- Mean mode
- Kind mode
- Normal mode
- `!mean`
- `!kind`
- `!mode`
- Server conversations without needing to mention the bot
- Direct messages
- Conversation memory
- Image/GIF understanding
- Discord usernames and server information
- Typing indicator
- Per-user cooldown
- Gemini API rate-limit handling
- `.env` configuration

---

# Chromebook Linux Setup

This guide is specifically for **Chromebook Linux (Linux development environment)**.

## 1. Open the Linux Terminal

On your Chromebook:

**Settings → Advanced → Developers → Linux development environment**

Make sure Linux is enabled.

Then open the **Terminal** app.

---

## 2. Install Python, Git, and pip

Run:

```bash
sudo apt update
Then:

sudo apt install python3 python3-pip python3-venv git -y

Check Python:

python3 --version

Check Git:

git --version

Python 3.12 or newer is recommended.

3. Download the Bot

Clone the GitHub repository:

git clone https://github.com/Kebrondawit13/discord-ai-bot.git

Enter the bot folder:

cd discord-ai-bot
4. Create a Virtual Environment

Create a Python virtual environment:

python3 -m venv venv

Activate it:

source venv/bin/activate

You should see (venv) at the beginning of your terminal.

Example:

(venv) user@penguin:~/discord-ai-bot$
5. Install the Required Libraries

Install everything from requirements.txt:

python -m pip install -r requirements.txt

The bot requires:

discord.py
google-genai
python-dotenv

You do not need to install these manually.

Discord Bot Setup
6. Create a Discord Application

Go to:

https://discord.com/developers/applications

Click:

New Application

Give the application a name.

Then open:

Bot → Add Bot

Copy the bot token.

Never share your bot token with anyone.

7. Enable Discord Intents

In the Discord Developer Portal, open:

Bot → Privileged Gateway Intents

Enable:

Message Content Intent
Server Members Intent

Click Save Changes.

8. Invite the Bot to Your Server

Open:

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

Open it in your browser, select your server, and authorize the bot.

Gemini Setup
9. Get a Gemini API Key

Go to:

https://aistudio.google.com/apikey

Create a Gemini API key.

Keep this key private.

Bot Configuration
10. Create .env

Inside the discord-ai-bot folder, create a file named:

.env

You can create it with:

nano .env

Put this inside:

DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Replace:

YOUR_DISCORD_BOT_TOKEN

with your Discord bot token.

Replace:

YOUR_GEMINI_API_KEY

with your Gemini API key.

Save the file.

If using nano:

CTRL + O

Press Enter, thenRunning the Bot
12. Activate the Virtual Environment

Every time you open a new terminal, run:

cd discord-ai-bot

Then:

source venv/bin/activate
13. Start the Bot

Run:

python ai.py

If everything is configured correctly, the bot will log in and appear online in Discord.

Keep the terminal running while you want the bot online.

To stop the bot:

CTRL + C
Commands

The bot uses the ! prefix.

Normal Mode
!mode

Changes the bot to normal mode.

Mean Mode
!mean

Changes the bot to mean mode.

Kind Mode
!kind

Changes the bot to kind mode.

Do not use /mean, /kind, or /mode.

Talking to the Bot

The bot can respond to messages in supported Discord channels.

It can also be used through direct messages.

The bot uses recent conversation history to help maintain context.

Image and GIF Understanding

The bot can process supported images and GIFs sent through Discord and use Gemini to understand their contents.

Updating the Bot

To update your local copy to the newest GitHub version:

cd discord-ai-bot

Pull the latest changes:

git pull

Activate the virtual environment:

source venv/bin/activate

Update the dependencies:

python -m pip install -r requirements.txt

Start the bot again:

python ai.py
Troubleshooting
Python is not installed

Run:

sudo apt update

Then:

sudo apt install python3 python3-pip python3-venv -y

Check Python:

python3 --version
pip gives an error

Make sure the virtual environment is activated:

source venv/bin/activate

Then:

python -m pip install -r requirements.txt
The bot is online but does not respond

Check:

Message Content Intent is enabled.
The bot has permission to view the channel.
The bot has permission to send messages.
Your Discord token is correct.
Your Gemini API key is correct.
.env is in the same folder as ai.py.
You restarted the bot after changing .env.
!mean, !kind, or !mode does not work

Make sure you use the ! prefix:

!mean
!kind
!mode

Do not use:

/mean
/kind
/mode
Project Structure
discord-ai-bot/
│
├── ai.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
Requirements
Chromebook
ChromeOS Linux development environment
Python 3.12+
Git
pip
Discord account
Discord bot application
Gemini API key
Internet connection
:

CTRL + X
