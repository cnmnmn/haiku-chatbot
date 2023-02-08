# This example requires the 'message_content' intent.

import discord

TOKEN = ' ' # TOKENを貼り付け
CHANNELID = 1066996682216177745 # チャンネルIDを貼り付け


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
    	if(message.author.bot):
        	return
    	else:
        	channel = client.get_channel(CHANNELID)
        	await channel.send(message.content)
        	print(message.content)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
