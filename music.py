import discord
from discord.ext import commands
import youtube_dl


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def j(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("hey friend, please connect to a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        await ctx.send("Hello there!")

    @commands.command()
    async def stop(self, ctx):
        if ctx.voice_channel.connect() is True:
            await ctx.voice_client.disconnect()
            await ctx.send("bye bye!")
        else:
            await ctx.send("I already have been disconnected!")

    @commands.command()
    async def p(self, ctx, url):
        ctx.voice_client.stop()
        FFMEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_channel.connect() is True:
            await ctx.voice_client.pause()
            await ctx.send("Paused!")
        else:
            await ctx.send("I'm not even connected!")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_channel.connect() is True and ctx.voice_client.pause() is True:
            await ctx.voice_client.resume()
            await ctx.send('Resuming!')
        else:
            ctx.send("There's nothing paused so we can resume!")


def setup(client):
    client.add_cog(Music(client))
