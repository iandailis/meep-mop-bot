import asyncio

import discord

from discord.ext import commands

class VoiceLines(commands.Cog):
	def __init__(self):
		pass
	
	@commands.command()
	async def mop(self, ctx, arg = 1):
		print("mop")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/meep mop.mp3"))
			await asyncio.sleep(.5)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()

	@commands.command()
	async def turtle(self, ctx, arg=1):
		print("turtle")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/turtle.mp3"))
			await asyncio.sleep(.3)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()


	@commands.command()
	async def herm(self, ctx, arg=1):
		print("herm")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/herm.mp3"))
			await asyncio.sleep(.5)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()

	@commands.command()
	async def HERM(self, ctx, arg=1):
		print("HERM")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/herm bass.mp3"))
			await asyncio.sleep(1)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()

	@commands.command()
	async def ivern(self, ctx, arg=1):
		print("ivern")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/ivern.mp3"))
			await asyncio.sleep(2)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()

	@commands.command()
	async def MOP(self, ctx, arg = 1):
		print("MEEPMOP")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/meep mop bass.mp3"))
			await asyncio.sleep(.7)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()

	@commands.command()
	async def moop(self, ctx, arg = 1):
		print("meeepmoop")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/meeepmooop.mp3"))
			await asyncio.sleep(3)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()

	@commands.command()
	async def maneuver(self, ctx, arg = 1):
		print("maneuver")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/maneuver.mp3"))
			await asyncio.sleep(2.8)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()

	@commands.command()
	async def bububu(self, ctx, arg = 1):
		print("bububu")
		for i in range (int(arg)):
			if (not ctx.voice_client):
				return
			ctx.voice_client.play(discord.FFmpegPCMAudio(source="assets/snapcall.mp3"))
			await asyncio.sleep(2.80)
			if (not ctx.voice_client):
				return
			ctx.voice_client.stop()
		await ctx.voice_client.disconnect()

	@mop.before_invoke
	@turtle.before_invoke
	@herm.before_invoke
	@HERM.before_invoke
	@MOP.before_invoke
	@moop.before_invoke
	@maneuver.before_invoke
	@bububu.before_invoke
	@ivern.before_invoke
	async def ensure_voice(self, ctx):
		if ctx.voice_client is None:
			if ctx.author.voice:
				await ctx.author.voice.channel.connect()
			else:
				await ctx.send("you not in voice")
				raise commands.CommandError("Author not connected to a voice channel.")
		elif (ctx.voice_client.is_playing()):
			await ctx.send("stop current audio first before playing new voice line")

	@staticmethod
	def getCommands():
		commands = [
			"<voiceline> <iterations> -- play <voiceline> <iterations> times\n available voicelines:",
			"mop",
			"MOP",
			"turtle",
			"herm",
			"HERM",
			"ivern",
			"maneuver",
			"bububu"
		]
		return commands
