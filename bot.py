import discord
import keyboard
import asyncio
from discord.ext import commands
import speech_recognition as sr
import pyaudio
from pytube import YouTube
from pytube import Search
import io

TOKEN = 
client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
	print('Ready')

@client.command()
async def play(ctx, *arg):
	if ctx.message.author.voice:
		print("play")

		query = ""
		for word in arg:
			query += word + " "
		query = query.rstrip()  

		print("searching for " + query + ", ", end="")
		s = Search(query)
		yt = s.results[0]
		print("found " + str(s.results[0]) + ", ", end="")
		stream = yt.streams.get_audio_only()
		stream.download(filename="music.mp4")
		print("downloaded " + str(stream))

		channel = ctx.message.author.voice.channel
		vc = await channel.connect()

		url = "https://www.youtube.com/watch?v=" + str(yt)[41:-1]
		await ctx.send("playing: " + url)

		vc.play(discord.FFmpegOpusAudio(source="music.mp4"))
		await asyncio.sleep(yt.length)
		await vc.disconnect()

@client.command()
async def turtle(ctx, arg=1):
	if ctx.message.author.voice:
		print("turtle")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/turtle.mp3"))
			await asyncio.sleep(.3)
			vc.stop()
		await vc.disconnect()


@client.command()
async def herm(ctx, arg=1):
	if ctx.message.author.voice:
		print("herm")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/herm.mp3"))
			await asyncio.sleep(.5)
			vc.stop()
		await vc.disconnect()

@client.command()
async def HERM(ctx, arg=1):
	if ctx.message.author.voice:
		print("HERM")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/herm bass.mp3"))
			await asyncio.sleep(1)
			vc.stop()
		await vc.disconnect()

@client.command()
async def ivern(ctx, arg=1):
	if ctx.message.author.voice:
		print("ivern")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/ivern.mp3"))
			await asyncio.sleep(2)
			vc.stop()
		await vc.disconnect()

@client.command()
async def listenmeep(ctx):
	if ctx.message.author.voice:
		print("listenmeep")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect()
		while True:
			try: 
				r = sr.Recognizer()
				mic = sr.Microphone()  # you want stereo mix (device_index=2)
				with mic as source:
					r.adjust_for_ambient_noise(source, duration=0.5)
					r.dynamic_energy_threshold = True
					audio = r.listen(source, timeout=2)
					r.pause_threshold = 0.5 
				words = r.recognize_google(audio, language='en-US')
				print(str(words))
				wordList = str(words).split(' ')
				for i in range (len(wordList)):
					if (('minion' == wordList[i]) or ('Minion' == wordList[i])):
						vc.play(discord.FFmpegPCMAudio(source="assets/meep mop.mp3"))
						await asyncio.sleep(.5)
						vc.stop()
					if (('cannon' == wordList[i]) or ('canon' == wordList[i]) or ('Cannon' == wordList[i]) or ('Canon' == wordList[i])):
						vc.play(discord.FFmpegPCMAudio(source="assets/meep mop bass.mp3"))
						await asyncio.sleep(.7)
						vc.stop()
					if (('stop listening' == wordList[i])):
						server = ctx.message.guild.voice_client
						await server.disconnect()
						break
			except Exception as oops:
				print(type(oops))
				pass

@client.command()
async def meepmop(ctx, arg = 1):
	if ctx.message.author.voice:
		print("meepmop")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/meep mop.mp3"))
			await asyncio.sleep(.5)
			vc.stop()
		await vc.disconnect()

@client.command()
async def MEEPMOP(ctx, arg = 1):
	if ctx.message.author.voice:
		print("MEEPMOP")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/meep mop bass.mp3"))
			await asyncio.sleep(.7)
			vc.stop()
		await vc.disconnect()

@client.command()
async def meeepmoop(ctx, arg = 1):
	if ctx.message.author.voice:
		print("meeepmoop")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/meeepmooop.mp3"))
			await asyncio.sleep(3)
			vc.stop()
		await vc.disconnect()

@client.command()
async def maneuver(ctx, arg = 1):
	if ctx.message.author.voice:
		print("maneuver")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/maneuver.mp3"))
			await asyncio.sleep(2.8)
			vc.stop()
		await vc.disconnect()

@client.command()
async def bubububu(ctx, arg = 1):
	if ctx.message.author.voice:
		print("bubububu")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/snapcall.mp3"))
			await asyncio.sleep(2.80)
			vc.stop()
		await vc.disconnect()

@client.command()
async def bububu(ctx, arg = 1):
	if ctx.message.author.voice:
		print("bububu")
		channel = ctx.message.author.voice.channel
		vc = await channel.connect() 
		for i in range (int(arg)):
			vc.play(discord.FFmpegPCMAudio(source="assets/snapcall.mp3"))
			await asyncio.sleep(2.80)
			vc.stop()
		await vc.disconnect()

@client.command()
async def meepstop(ctx):
	print("meepstop")
	server = ctx.message.guild.voice_client
	await server.disconnect()

client.run(TOKEN)
