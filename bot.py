import discord, time
from config import * # Import all the config file

class Client(discord.Client):
	async def on_ready(self):
		while(True):
			time.sleep(10)
			channel = self.get_channel(channel_id)
			await channel.send("!d bump")

Client().run(user_token, bot=False)
