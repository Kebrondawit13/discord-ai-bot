# Gemini Discord AI Bot

A Discord AI bot powered by Google's Gemini API.

This version is designed for **Chromebook Linux**.

## What it can do

- Talk using Google's Gemini AI
- Normal mode
- Kind mode
- Mean mode
- Conversation memory
- Understand images and GIFs
- Respond in Discord channels
- Respond to DMs
- Know Discord usernames and server information
- Typing indicator
- User cooldown
- Gemini API rate-limit handling

## Commands

```text
!mode
!kind
!mean
!mode = Normal mode
!kind = Kind mode
!mean = Mean mode

Important: These are ! commands, not / commands.

Installation
Before you start

You need:

A Chromebook
Linux enabled on your Chromebook
A Discord account
A Discord server where you can add bots
A Google account
An internet connection

Don't worry if you have never installed a Python bot before. Just follow the steps in order.

Step 1 — Turn on Linux

On your Chromebook:

Open Settings
Go to Advanced
Go to Developers
Find Linux development environment
Turn it on
Open the Terminal app

You will use the Terminal for the rest of the installation.

Step 2 — Install Python and Git

Copy this entire command into Terminal:

sudo apt update && sudo apt install python3 python3-pip python3-venv git -y

Wait until it finishes.

Now check Python:

python3 --version

You should see something similar to:

Python 3.x.x

Also check Git:

git --version

If both commands work, continue.

Step 3 — Download the Bot

Copy this command:

git clone https://github.com/Kebrondawit13/discord-ai-bot.git

Then enter the bot folder:

cd discord-ai-bot

Your terminal should now be inside the bot folder.

Step 4 — Create the Python Environment

Copy:

python3 -m venv venv

Then activate it:

source venv/bin/activate

You should now see:

(venv)

at the beginning of your terminal.

For example:

(venv) user@penguin:~/discord-ai-bot$

If you see (venv), you're ready.

Step 5 — Install the Bot's Libraries

Copy:

python -m pip install -r requirements.txt

Wait for it to finish.

The bot automatically installs these libraries:

discord.py
google-genai
python-dotenv

You don't need to install them separately.

Step 6 — Create Your Discord Bot

Now you need to create the actual Discord bot.

Go here:

https://discord.com/developers/applications

Create the application
Click New Application
Give your bot a name
Click Create
Open Bot on the left
Click Add Bot

You now have a Discord bot.

Step 7 — Get Your Discord Bot Token

On the Bot page:

Find the Token section
Click Reset Token or Copy
Save the token somewhere temporarily

NEVER post your bot token publicly.

Your token gives access to your bot.

If someone gets your token, they can control your bot.

Step 8 — Enable Discord Intents

Still on the Bot page, find:

Privileged Gateway Intents

Turn on:

Message Content Intent
Server Members Intent

Then click:

Save Changes

Step 9 — Add the Bot to Your Server

Go to:

OAuth2 → URL Generator

Under scopes, select:

bot

Then give it these permissions:

View Channels
Send Messages
Read Message History
Embed Links
Attach Files

Copy the generated URL at the bottom.

Open that URL in your browser.

Select your Discord server and click Authorize.

Your bot should now be inside your server.

Step 10 — Get Your Gemini API Key

The bot uses Google's Gemini API.

Go here:

https://aistudio.google.com/apikey

Create an API key.

Copy the key.

Keep your Gemini API key private.

Step 11 — Create the .env File

Go back to your Chromebook Terminal.

Make sure you are inside the bot folder:

cd ~/discord-ai-bot

Create the .env file:

nano .env

Paste this:

DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Now replace:

YOUR_DISCORD_BOT_TOKEN

with your Discord bot token.

And replace:

YOUR_GEMINI_API_KEY

with your Gemini API key.

For example:

DISCORD_BOT_TOKEN=your_actual_discord_token_here
GEMINI_API_KEY=your_actual_gemini_key_here

Do not use the example values above as actual keys.

Step 12 — Save .env

If you are using nano:

Press:

CTRL + O

Press:

ENTER

Then press:

CTRL + X

You should return to the Terminal.
Step 13 — Start the Bot

Make sure your virtual environment is activated.

If you don't see (venv), run:

cd ~/discord-ai-bot
source venv/bin/activate

Then start the bot:

python ai.py

If everything is configured correctly, you should see messages showing that the bot logged in.

Your bot should appear online in Discord.

Step 14 — Test the Bot

Go to your Discord server.

Try:

!mode

The bot should switch to Normal mode.

Try:

!kind

The bot should switch to Kind mode.

Try:

!mean

The bot should switch to Mean mode.

Then send a normal message and talk to the bot.

Important: Use !, Not /

The bot uses prefix commands.

Correct:

!mode
!kind
!mean

Wrong:

/mode
/kind
/mean

If you type /, these commands will not appear because they are not Discord slash commands.

Keeping the Bot Online

The bot only stays online while the Python program is running.

Keep the Chromebook Terminal open and leave this running:

python ai.py

If you close the Terminal or stop the program, the bot goes offline.

To stop the bot yourself:

CTRL + C
Starting the Bot Again Later

When you turn your Chromebook back on, open Terminal and run:

cd ~/discord-ai-bot

Activate the environment:

source venv/bin/activate

Start the bot:

python ai.py

That's it.
