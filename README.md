# meep-mop-bot
discord bot with speech recognition and youtube audio streaming.

Requirements:
discord
SpeechRecognition + PyAudio (needed for recognition)
PyTube

also ffmpeg needs to be on PATH

and maybe some other stuff. errors will tell you.

Generate your own Discord API token, put it in the top of bot.py, then run with python3.

Commands:

* meepmop arg (arg optional) - joins voice channel, says "meepmop" arg times or 1 if arg ommitted then leaves.
* play arg - queries youtube with arg, then after downloading the audio plays it in the voice channel.
* listenmeep - joins voice channel, listens for "cannon" or "minion" then plays the appropriate sound. 
* meepstop - stop the currently playing audio or listenmeep

Enjoy! -Ian D
