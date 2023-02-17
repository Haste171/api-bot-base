# Api Bot Base

This is a Python Discord bot that interacts with an external API

## Installation

To run this bot, you'll need to do the following:

1. Clone the repository to your local machine
2. Install the required packages by running `pip install -r requirements.txt`
3. Create a `.env` file with the following environment variables seen in .env.example:
   - `BOT_TOKEN`: Your Discord bot token
   - `API_KEY`: Your API key
4. Start the bot by running `python main.py`

## Usage

The bot has one command you can base your others off of:

- `/example variable`: Makes a request to an external API using the specified variable

To use these commands, simply enter them in a Discord text channel where the bot is present
