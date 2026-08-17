# Gemini Discord AI Bot

# A Discord AI bot powered by Google's Gemini API with personality modes, vision capabilities, and memory.

# Features

# Gemini-Powered Conversations: Advanced AI responses in server channels and direct messages.
# Personality Modes:
# !mode - Normal Mode
# !mean - Mean Mode
# !kind - Kind Mode
# No Mention Needed: Engages naturally in designated channels.
# Vision Support: Image and GIF analysis via Gemini.
# Context Memory: Remembers recent conversation history per user.
# Built-in Guardrails: Per-user cooldowns and Gemini API rate-limit handling.

# Prerequisites

# Chromebook with ChromeOS Linux development environment enabled
# Python 3.12+
# Git and pip
# Discord Account & Developer Application
# Gemini API Key

# Chromebook Linux Setup

# Follow these steps in order.

# 1. Enable Linux Environment

# 1. On your Chromebook, go to Settings -> Advanced -> Developers -> Linux development environment.
# 2. Turn Linux on.
# 3. Open the Terminal app from your app drawer.

# 2. Install Python and Git

# Run the following command in your terminal:

# sudo apt update && sudo apt install python3 python3-pip python3-venv git -y

# Verify the installations:

# python3 --version
# git --version

# 3. Download the Bot

# Clone the repository and enter the directory:

# git clone https://github.com/Kebrondawit13/discord-ai-bot.git
# cd discord-ai-bot

# 4. Set Up Python Virtual Environment

# Create and activate the environment:

# python3 -m venv venv
# source venv/bin/activate

# (You should now see (venv) at the start of your terminal prompt).

# 5. Install Dependencies

# Install all required Python packages at once:

# python -m pip install -r requirements.txt

# API & Bot Setup

# 6. Create Your Discord Bot

# 1. Go to the Discord Developer Portal (https://discord.com/developers/applications).
# 2. Click New Application and set a name.
# 3. Navigate to Bot -> Add Bot.
# 4. Click Reset Token and copy your Bot Token. (Keep this token private!)

# 7. Enable Gateway Intents

# In the Developer Portal under Bot -> Privileged Gateway Intents, enable:
# Message Content Intent
# Server Members Intent

# Click Save Changes.

# 8. Invite the Bot to Your Server

# 1. Go to OAuth2 -> URL Generator.
# 2. Select the bot scope.
# 3. Under Bot Permissions, select:
# View Channels
# Send Messages
# Read Message History
# Embed Links
# Attach Files
# 4. Copy the generated URL at the bottom, paste it into your browser, and select your server.

# 9. Get a Gemini API Key

# 1. Go to Google AI Studio (https://aistudio.google.com/apikey).
# 2. Click Create API Key.
# 3. Copy your API key.

# Configuration & Launch

# 10. Create the .env File

# Inside the discord-ai-bot folder, open the nano editor:

# nano .env

# Paste the following and replace the placeholder text with your actual keys:

# DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
# GEMINI_API_KEY=YOUR_GEMINI_API_KEY

# Save and exit:
# Press CTRL + O, then Enter (Save)
# Press CTRL + X (Exit)

# Note: Never commit or upload your .env file to GitHub.

# 11. Run the Bot

# To start the bot anytime:

# cd ~/discord-ai-bot
# source venv/bin/activate
# python ai.py

# Keep the terminal window open while running. Press CTRL + C to stop the bot.

# Usage & Commands

# Use the ! prefix to trigger commands in Discord:

# !mode - Normal Mode (Standard, helpful Gemini interactions)
# !mean - Mean Mode (Sarcastic and witty responses)
# !kind - Kind Mode (Warm and overly encouraging responses)

# Note: Slash commands (e.g., /mode) are not supported.

# Updating the Bot

# To pull the latest updates from GitHub:

# cd ~/discord-ai-bot
# source venv/bin/activate
# git pull
# python -m pip install -r requirements.txt
# python ai.py

# Troubleshooting

# Bot fails to start: Ensure venv is activated (source venv/bin/activate) and your .env file is in the root directory.
# Bot is online but doesn't reply:
# 1. Verify Message Content Intent is enabled in the Developer Portal.
# 2. Confirm the bot has read/write permissions in that channel.
# 3. Ensure your API keys in .env are accurate without extra spaces.

# Project Structure

# discord-ai-bot/
# │
# ├── ai.py
# ├── requirements.txt
# ├── .env.example
# ├── .gitignore
# └── README.md
