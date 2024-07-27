# Event and commands handler

import discord
from discord.ext import commands
import os
import os
import json

# Functions to load config files
def load_config():
    with open('config/config.json') as config_file:
        return json.load(config_file)
config = load_config()

# Config variables
BOT_TOKEN = config['BOT_TOKEN']
BOT_NAME = config['BOT_NAME']
BOT_PREFIX = config['BOT_PREFIX']
UsePresence = config['UsePresence']
PresenceMessage = config['PresenceMessage']

# Load the client intents
intents = discord.Intents.default()
intents.message_content = True

# Create a function to load the bot extensions
async def load_extensions(bot):
    for filename in os.listdir('./src/commands/'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'src.commands.{filename[:-3]}')
            except Exception as e:
                print(f'Failed to load extension {filename[:-3]}: {e}')

# Create an event that initialize the client
def create_bot():
    bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)
    @bot.event
    async def on_ready():
        if UsePresence:
            await bot.change_presence(activity=discord.Game(name=PresenceMessage))
        print(f'Client [{BOT_NAME}] initialized, logged in as {bot.user}:{bot.shard_id} | Total shards: {bot.shard_count}')

    return bot

async def main():
    bot = create_bot()
    await load_extensions(bot)
    token = BOT_TOKEN
    await bot.start(token)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())