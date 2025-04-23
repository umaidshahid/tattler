# 🔔 Voice Activity Notifier Discord Bot

This is a simple Discord bot that notifies a selected text channel whenever someone joins a voice channel. Useful for gaming servers, study sessions, or community hangouts.

## ✨ Features

- Sends a message when someone **joins a voice channel**
- Allows server admins to **set the text channel** for notifications via a `/setchannel` slash command
- Uses a dropdown menu for easy channel selection

> 💡 This bot does **not** notify when users leave a voice channel (by design).

## 🛠️ Requirements

- Python 3.10+
- A Discord bot token (from the [Discord Developer Portal](https://discord.com/developers/applications))
- `discord.py` library

## 📦 Installation

```bash
git clone https://github.com/your-username/voice-notifier-bot.git
cd voice-notifier-bot
pip install -r requirements.txt
