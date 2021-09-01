# Location for all the main (and important) code
# Run the bot from this file!!!

# Import all the important dependencies
import discord
from discord.ext import commands
from discord.utils import get

import asyncio
import json
import time
import random

# File Dependencies
import authkey

# Initalize bot information
client = commands.Bot(command_prefix='!')
token = authkey.authkey

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f"{message.author.name}: {message.content}")
    await client.process_commands(message)

@client.command(pass_context=True)
async def sayhi(ctx):
    await ctx.channel.send(f"Hi {ctx.author.nick}!")

client.run(token)
