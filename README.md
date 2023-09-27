# Telegram Wikipedia Bot

This is a simple Telegram bot that uses the Wikipedia API to retrieve summaries of topics. Users can send a command to the bot and provide a topic they want to research, and the bot will respond with a summary from Wikipedia.

## Features

- Get a summary of a topic from Wikipedia.
- Handle cases where the topic is not found or is ambiguous.

## Requirements

- Python 3.x
- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI)
- [Wikipedia API](https://pypi.org/project/wikipedia-api/)

## Getting Started

1. Clone the repository:

```bash
   git clone https://github.com/yourusername/telegram-wikipedia-bot.git
   cd telegram-wikipedia-bot
```
2. Install the required packages:

```bash
pip install telebot wikipedia-api
Set up your Telegram bot token as an environment variable:
```
```bash
export BOT_TOKEN=your_bot_token_here
```
3. Run the bot:

```bash
python bot.py
```
## Usage
Start a chat with the bot on Telegram.
Use the following commands to interact with the bot:
```bash
/start: Get a welcome message.
/help: Get information on how to use the bot.
/get <topic>: Retrieve a summary of the specified topic from Wikipedia.
Example
User: /get Python programming

Bot: Returns a summary of the topic "Python programming" from Wikipedia.
```
## License
This project is licensed under the MIT License.
