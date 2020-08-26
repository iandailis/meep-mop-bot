import discord
import keyboard
import asyncio
from discord.ext import commands
import speech_recognition as sr
import pyaudio

TOKEN = ' << DISCORD API TOKEN HERE >> '
client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
    print('Ready')
    
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
                        vc.play(discord.FFmpegPCMAudio(executable="C:/Users/Ian/Downloads/ffmpeg/bin/ffmpeg.exe", source="meep mop.mp3"))
                        await asyncio.sleep(.5)
                        vc.stop()
                    if (('cannon' == wordList[i]) or ('canon' == wordList[i]) or ('Cannon' == wordList[i]) or ('Canon' == wordList[i])):
                        vc.play(discord.FFmpegPCMAudio(executable="C:/Users/Ian/Downloads/ffmpeg/bin/ffmpeg.exe", source="meep mop bass.mp3"))
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
            vc.play(discord.FFmpegPCMAudio(executable="C:/Users/Ian/Downloads/ffmpeg/bin/ffmpeg.exe", source="meep mop.mp3"))
            await asyncio.sleep(.5)
            vc.stop()
        server = ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def MEEPMOP(ctx, arg = 1):
    if ctx.message.author.voice:
        print("MEEPMOP")
        channel = ctx.message.author.voice.channel
        vc = await channel.connect() 
        for i in range (int(arg)):
            vc.play(discord.FFmpegPCMAudio(executable="C:/Users/Ian/Downloads/ffmpeg/bin/ffmpeg.exe", source="meep mop bass.mp3"))
            await asyncio.sleep(.7)
            vc.stop()
        server = ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def meeepmoop(ctx, arg = 1):
    if ctx.message.author.voice:
        print("meeepmoop")
        channel = ctx.message.author.voice.channel
        vc = await channel.connect() 
        for i in range (int(arg)):
            vc.play(discord.FFmpegPCMAudio(executable="C:/Users/Ian/Downloads/ffmpeg/bin/ffmpeg.exe", source="meeepmooop.mp3"))
            await asyncio.sleep(3)
            vc.stop()
        server = ctx.message.guild.voice_client
        await server.disconnect()

@client.command()
async def meepstop(ctx):
    print("meepstop")
    server = ctx.message.guild.voice_client
    await server.disconnect()

client.run(TOKEN)
