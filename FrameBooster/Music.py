import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #all the music related stuff
        self.is_playing = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""

     #searching the item on youtube
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            #get the first url
            m_url = self.music_queue[0][0]['source']

            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    # infinite loop checking
    async def play_music(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            #try to connect to voice channel if you are not already connected

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])

            print(self.music_queue)
            #remove the first element as you are currently playing it
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name="play", help="Jouer une vidéo Youtube: %play <ta musique>")
    async def play(self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            #you need to be connected so that the bot knows where to go
            await ctx.send("**/❗️/❕/- - -** Tu dois te connecter à un salon vocal ! **- - -/❗️/❕/**")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("**/❗️/❕/- - -** Impossible de lire la vidéo **- - -/❗️/❕/**")
            else:
                await ctx.send("**/🎵/🎶/- - - ** Ta musique à été ajouté à la file d'attente ;) ** - - -/🎵/🎶/**")
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music()
    @commands.command(name="p", help="Jouer une vidéo Youtube: %play <ta musique>")
    async def p(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            #you need to be connected so that the bot knows where to go
            await ctx.send("**/❗️/❕/- - -** Tu dois te connecter à un salon vocal ! **- - -/❗️/❕/**")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("**/❗️/❕/- - -** Impossible de lire la vidéo **- - -/❗️/❕/**")
            else:
                await ctx.send("**/🎵/🎶/- - - ** Ta musique à été ajouté à la file d'attente ;) ** - - -/🎵/🎶/**")
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music()

    @commands.command(name="queue", help="Voir la file d'attente")
    async def queue(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"
    @commands.command(name="q", help="Voir la file d'attente")
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += self.music_queue[i][0]['title'] + "\n"


    @commands.command(name="skip", help="Mettre la prochaine musique")
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music()
    @commands.command(name="next", help="Mettre la prochaine musique")
    async def next(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music()
    @commands.command(name="n", help="Mettre la prochaine musique")
    async def n(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music()
    @commands.command(name="s", help="Mettre la prochaine musique")
    async def s(self, ctx):
        if self.vc != "" and self.vc:
            self.vc.stop()
            #try to play next in the queue if it exists
            await self.play_music()

    @commands.command(name="disconnect", help="déconnecter le bot  du salon vocal")
    async def dc(self, ctx):
        await self.vc.disconnect()
    @commands.command(name="disc", help="déconnecter le bot  du salon vocal")
    async def disc(self, ctx):
        await self.vc.disconnect()
