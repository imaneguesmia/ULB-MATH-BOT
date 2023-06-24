#!/usr/bin/env python3

import discord

with open("TOKEN.txt", 'r') as f:
    TOKEN = f.read().strip()


# v the basic code taken straight from discord.py's documentation
class MyClient(discord.Client):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.role_message_id = 1122212168528576512
    async def on_ready(self):
        print("YO! ! ! !!!")
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content[:2].lower() == "yo":
            await message.channel.send('HULLO')
    async def on_raw_reaction_add(self,payload):
        if payload.message_id != self.role_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        role = None
        if payload.emoji.name == "🟣":
            role = discord.utils.get(guild.roles,name="BOB")
        elif payload.emoji.name == "🔵":
            role = discord.utils.get(guild.roles,name="BOBETTE")
        if role is not None:
            await payload.member.add_roles(role)
    async def on_raw_reaction_remove(self,payload):
        if payload.message_id != self.role_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = None
        if payload.emoji.name == "🟣":
            role = discord.utils.get(guild.roles,name="BOB")
        elif payload.emoji.name == "🔵":
            role = discord.utils.get(guild.roles,name="BOBETTE")

        if role is not None:
            await member.remove_roles(role)



intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
