import asyncio

import discord
import youtube_dl

from discord.ext import commands

ytdl_format_options = {
	'format': 'bestaudio/best',
	'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
	'restrictfilenames': True,
	'noplaylist': True,
	'nocheckcertificate': True,
	'ignoreerrors': False,
	'logtostderr': False,
	'quiet': True,
	'no_warnings': True,
	'rm-cache-dir': True,
	'default_search': 'auto',
	'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues 
}

ffmpeg_options = {
	'options': '-vn'
}

class YoutubePlayer(commands.Cog):
	def __init__(self):
		self.queue = []
		self.currentAudioTask = 0
		self.vc = 0

	@commands.command()
	async def queue(self, ctx, *arg):
		print("queue")
		async with ctx.typing():
			if (len(self.queue) == 0):
				await ctx.send("queue is empty")
			else:
				message = ""
				for i in range(len(self.queue)):
					message += str(i) + ": " + self.queue[i]['title'] + " <" + self.__getURL(self.queue[i]['id']) + ">\n"
				await ctx.send(message)

	@commands.command()
	async def move(self, ctx, arg=1):
		print("move")
		async with ctx.typing():
			index = int(arg)
			if (index <= 1 or index >= len(self.queue)):
				await ctx.send("index out of range")
				return
			self.queue.insert(1, self.queue[index])
			self.queue.pop(index + 1)
			await ctx.send("moved " + self.queue[1]['title'] + " to front of queue")

	@commands.command()
	async def remove(self, ctx, arg=1):
		print("remove")
		async with ctx.typing():
			index = int(arg) # convert string

			# check if valid index
			if (index < 0 or index >= len(self.queue)):
				await ctx.send("invalid index")
				return

			# skip the currently playing audio if removing the 0th item
			if (index == 0): 
				await self.skip(ctx)

			# simply remove the entry otherwise
			else:
				self.queue.pop(index)
				await ctx.send("removed " + self.queue[index]['title'])

	@commands.command()
	async def stop(self, ctx):
		async with ctx.typing():
			print("stop")
			if (self.currentAudioTask):	
				self.queue = []
				self.currentAudioTask.cancel()
			else:
				await ctx.voice_client.disconnect()
	
	@commands.command()
	async def skip(self, ctx):
		print("skip")
		async with ctx.typing():
			if (len(self.queue) == 0): # invalid input check
				await ctx.send("nothing is playing")

			else: # cancel the task, skipping the song
				await ctx.send("skipped " + self.queue[0]['title'])
				self.currentAudioTask.cancel()

	@commands.command()
	async def play(self, ctx, *arg):
		print("play" + str(arg))
		async with ctx.typing(): # bot types while finding audio
			# parse arg list into space separated string
			query = " ".join(word for word in arg)
			
			# get the audio data
			audioMetadata = self.__search(query)
			
			# if a playlist was found, add the entire playlist
			if 'entries' in audioMetadata:
				for entry in audioMetadata['entries']:
					self.queue.append(entry)
				await ctx.send("added " + str(len(audioMetadata['entries'])) + " entries from " + arg[0])
			else: # otherwise just add the one found entry
				self.queue.append(audioMetadata)
				await ctx.send(str(len(self.queue)-1) + ": " + self.__getURL(audioMetadata['id']))

		# connect to a voice client if not connected already
		if ctx.voice_client is None:
			await self.vc.connect()
			# create the audio player task
			asyncio.get_event_loop().create_task(self.__player(ctx))

	async def __player(self, ctx):
		while (len(self.queue) > 0):
			# make a new task to play the audio
			self.currentAudioTask = asyncio.get_event_loop().create_task(self.__playAudio(ctx))
			# wait for the audio to finish before starting the next one
			await asyncio.gather(self.currentAudioTask)

		# cleanup and disconnect
		self.currentAudioTask = 0
		await ctx.voice_client.disconnect()
		self.vc = 0

	async def __playAudio(self, ctx):
		print("ok we go")
		# get the encoded audio player
		player = discord.FFmpegOpusAudio(self.queue[0]['url'], **ffmpeg_options)

		# stop any playing audio first just in case
		ctx.voice_client.stop()	
		# play the audio
		ctx.voice_client.play(player)

		try: # wait until the audio is done or is skipped
			await asyncio.sleep(self.queue[0]['duration'])

		except asyncio.CancelledError:	# invoked when the audio is skipped, 
			ctx.voice_client.stop()		# which is when this task is canceled

		# remove self from the queue
		try:
			self.queue.pop(0)
		except IndexError: # needed so stop doesn't cause an exception
			pass

	@staticmethod
	def getCommands():
		commands = [
			"play <query or link to video/playlist> -- adds a youtube video or playlist to a queue then plays it",
			"queue -- see the current play queue",
			"move <index> -- move an entry to the top of the queue",
			"skip --  skips the currently playing video",
			"remove <index> -- remove a video from the queue at the given index",
			"stop -- clear the queue and stop playback"
		]
		return commands

	@staticmethod
	def __getURL(id):
		return "https://www.youtube.com/watch?v=" + id
	
	@staticmethod
	def __search(arg):
		with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
			try: # check if the argument was a video URL
				get(arg)
			except: # on exception, the argument is not a URL, so get the first search result
				if (arg[0:33] == "https://www.youtube.com/playlist?"):
					video = ydl.extract_info(arg, download=False)
				else:
					video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
			else: # no exception when the argument is a URL, so just get the video from the URL
				video = ydl.extract_info(arg, download=False)
		return video

	# these directives mean that the below function is called before any of these functions
	@play.before_invoke
	@queue.before_invoke
	@move.before_invoke
	@skip.before_invoke
	@remove.before_invoke
	@stop.before_invoke
	async def checkAuthor(self, ctx):
		# check that the message author is in a voice channel and in the current voice channel
		if (not ctx.author.voice):
			await ctx.send("you not in voice")
			raise commands.CommandError("Author not connected to a voice channel.")
		if (self.vc and self.vc != ctx.author.voice.channel):
			await ctx.send("you not in current voice")
			raise commands.CommandError("Author not connected to current voice channel.")

		# set current voice channel
		if (not self.vc):
			self.vc = ctx.author.voice.channel
