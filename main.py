import time
import os
from twitchio.ext import commands
import keyboard
import mouse

os.system('Celeste Twitch Controller')

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='#### ACCESS TOKEN ####', prefix='!', initial_channels=['itserif'])
        
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        

    @commands.command()
    async def controls(self, ctx: commands.Context):
      await ctx.send(f'Controls = !u !d !l !r !jump !dash !rjump !ljump {ctx.author.name}!')

    @commands.command()
    async def u(self, ctx: commands.Context):
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')

    @commands.command()
    async def l(self, ctx: commands.Context):
        keyboard.press('a')
        time.sleep(1)
        keyboard.release('a')

    @commands.command()
    async def d(self, ctx: commands.Context):
        keyboard.press('s')
        time.sleep(1)
        keyboard.release('s')

    @commands.command()
    async def r(self, ctx: commands.Context):
        keyboard.press('d')
        time.sleep(1)
        keyboard.release('d')

    @commands.command()
    async def jump(self, ctx: commands.Context):
        keyboard.press('space')
        time.sleep(1)
        keyboard.release('space')

    @commands.command()
    async def dash(self, ctx: commands.Context):
        keyboard.press('x')
        keyboard.press('z')
        time.sleep(0.4)
        keyboard.release('z')
        keyboard.release('x')

    @commands.command()
    async def rjump(self, ctx: commands.Context):
        keyboard.press('d')
        keyboard.press('space')
        time.sleep(0.4)
        keyboard.release('space')
        keyboard.release('d')

    @commands.command()
    async def ljump(self, ctx: commands.Context):
        keyboard.press('a')
        keyboard.press('space')
        time.sleep(0.4)
        keyboard.release('space')
        keyboard.release('a')

    @commands.command() 
    async def lookr(self, ctx: commands.Context):
       mouse.move(500, 0, absolute=False, duration=0.2)

    @commands.command() 
    async def lookl(self, ctx: commands.Context):
       mouse.move(500, 0, absolute=False, duration=0.2)

    @commands.command() 
    async def lookd(self, ctx: commands.Context):
       mouse.move(0, 500, absolute=False, duration=0.2)

    @commands.command() 
    async def looku(self, ctx: commands.Context):
       mouse.move(0, -500, absolute=False, duration=0.2)


bot = Bot()
bot.run()


