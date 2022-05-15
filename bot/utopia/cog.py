from discord.ext import commands
import httpx

class Utopia(commands.Cog):
    """Commands that are connected to Utopia"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def dragons(self, ctx, Target_Kingdom: str):
        """Stats on dragons target at a kingdom"""
        kingdom, island = Target_Kingdom.split(':')
        kd = f'{kingdom[:2]}/{island[:2]}'
        async with httpx.AsyncClient() as client:
            r = await client.get(f'https://chriso.no/utopia/api/dragons/{kd}')
        if r.status_code == 200:
            txt = r.text
        else:
            txt = 'Unable to fetch data.'
        await ctx.send(txt[:2000])


    @commands.command()
    async def kingdom(self, ctx, Target_Kingdom: str):
        """Infomation on a kingdom"""
        kingdom, island = Target_Kingdom.split(':')
        kd = f'{kingdom[:2]}/{island[:2]}'
        async with httpx.AsyncClient() as client:
            r = await client.get(f'https://chriso.no/utopia/api/kingdoms/{kd}')
        if r.status_code == 200:
            txt = r.text
        else:
            txt = 'Unable to fetch data.'
        await ctx.send(txt[:2000])


    @commands.command()
    async def plunder(self, ctx):
        """Kingdoms leaving war soon"""
        async with httpx.AsyncClient() as client:
            r = await client.get('https://chriso.no/utopia/api/plunder/')
        if r.status_code == 200:
            txt = r.text
        else:
            txt = 'Unable to fetch data.'
        await ctx.send(txt[:2000])


    @commands.command()
    async def war(self, ctx, Target_Kingdom: str):
        """Stats on a kingdom war"""
        kingdom, island = Target_Kingdom.split(':')
        kd = f'{kingdom[:2]}/{island[:2]}'
        async with httpx.AsyncClient() as client:
            r = await client.get(f'https://chriso.no/utopia/api/war/{kd}')
        if r.status_code == 200:
            txt = r.text
        else:
            txt = 'Unable to fetch data.'
        await ctx.send(txt[:2000])
