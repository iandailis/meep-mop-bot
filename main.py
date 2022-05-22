import asyncio

import discord

from discord.ext import commands

from src.YoutubePlayer import YoutubePlayer
from src.VoiceLines import VoiceLines

class MeepMopBot:
	def __init__(self):
		self.bot = commands.Bot(command_prefix=commands.when_mentioned_or("meep"))
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

	def add_cog(self, cog):
		self.cogs.append(cog)
		self.bot.add_cog(cog)

	def run(self, token):
		self.bot.run(token)


if (__name__ == "__main__"):
	with open("token.txt", 'r') as f:
		token = f.readlines()[0]

	bot = MeepMopBot()
	bot.add_cog(YoutubePlayer())
	bot.add_cog(VoiceLines())
	bot.run(token)
