import asyncio
import nest_asyncio
nest_asyncio.apply()

import discord

from discord.ext import commands

from src.YoutubePlayer import YoutubePlayer
from src.VoiceLines import VoiceLines

class MeepMopBot:
	def __init__(self):
		intents = discord.Intents.all()
		self.bot = commands.Bot(command_prefix=commands.when_mentioned_or("meep"), intents=intents)
		self.cogs = []

		self.bot.remove_command('help')

		@self.bot.event
		async def on_ready():
			print('Logged in as {0} ({0.id})'.format(self.bot.user) + "\n-----")

		@self.bot.command()
		async def help(ctx):
			for cog in self.cogs:
				try:
					commands = cog.getCommands()
					message = ""
					for entry in commands:
						message += "meep" + entry + "\n"
					await ctx.send(message)
				except:
					pass

	async def add_cog(self, cog):
		self.cogs.append(cog)
		await self.bot.add_cog(cog)

	async def run(self, token):
		await self.bot.run(token)

async def setup(token):
	bot = MeepMopBot()
	await bot.add_cog(YoutubePlayer())
	await bot.add_cog(VoiceLines())
	await bot.run(token)

if (__name__ == "__main__"):
	with open("token.txt", 'r') as f:
		token = f.readlines()[0]
	asyncio.run(setup(token))
