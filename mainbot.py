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

def new_json():
    with open('accounts/accounts.json') as read_file:
            accounts = json.load(read_file)
            return accounts

def finduser(username, accounts):
    location = 0
    for x in range (len(accounts)):
        if username == accounts[str(x)]['username']:
            location = x
            break
    return location

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
async def hi(ctx):
    await ctx.channel.send(f"Hi {ctx.author.nick}!")

@client.command(pass_context=True)
async def account(ctx):
    accounts = new_json()
    location = finduser(ctx.author.nick, accounts)
    if not location:
        await ctx.channel.send(f"Sorry, user not detected. Make sure you discord nickname is the same as your twitch username and try again!")
    else:
        points = accounts[str(location)]['points']
        xp = accounts[str(location)]['xp']
        message = f"Welcome back {accounts[str(location)]['username']}! You have [{xp}] xp and a balance of [{points}] points. Hello from Twitch!"
        await ctx.channel.send(message)

client.run(token)
