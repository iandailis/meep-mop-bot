import discord
import keyboard
import asyncio
from discord.ext import commands

TOKEN = 'NzQ0NjQ1NDE1ODQ4MjQ3MzI4.XzmPFQ.KQKoWqGMc18KUiLYkbNU6a1U120'
client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
    print('Ready')
    
@client.command()
async def meepmop(ctx, arg = 1):
    if ctx.message.author.voice:
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
    server = ctx.message.guild.voice_client
    await server.disconnect()

client.run(TOKEN)