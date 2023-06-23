#!/usr/bin/env python3

import discord

TOKEN = ""
with open("TOKEN.txt", 'r') as f:
    TOKEN = f.read().strip()


# v the basic code taken straight from discord.py's documentation
class MyClient(discord.Client):
    async def on_ready(self):
        print("YO! ! ! !!!")
    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
