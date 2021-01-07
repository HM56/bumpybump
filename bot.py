import discord
from asyncio import sleep
from config import *


class Client(discord.Client):
	active = True
	async def pauseBump(self):
		self.active = False
		print("Bump paused.")

	async def clean(self, user_message=None, bot_message=None):
		await sleep(3)
		if user_message is not None:
			await user_message.delete()
		if bot_message is not None:
			await bot_message.delete()
		print("Chat cleaned")

	async def continueBump(self):
		self.active = True
		print("Bump restored.")

	async def send(self, ctx, content):
		message = await ctx.channel.send(f"{ctx.author.mention} {content}")
		print(f"Sent '{content}' to '{ctx.author}'")
		await self.clean(ctx, message)

	async def bump(self):
		channel = self.get_channel(channel_id)
		command = await channel.send("!d bump")
		print("Server bumped")
		return command

	async def on_ready(self):
		print(f"Logged as {self.user}")
		while(self.active == True):
			command = await self.bump()
			await self.clean(command)
			await sleep(delay)

	async def on_message(self, message):
		if message.author == self.user:
			if message.content == "!pause":
				await self.pauseBump()
				await self.send(message, "Bot is paused :sleeping:")

			elif message.content == "!continue":
				await self.continueBump()
				await self.send(message, f"Bump is activated, next bump in {delay} seconds :hourglass_flowing_sand:")

Client().run(user_token, bot=False)
