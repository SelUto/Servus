import random
from discord.ext import commands

class Dice(commands.Cog):
    """Role a dice"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx):
        """Roles the dice."""
        await ctx.send(f'I roled **{random.choice(range(1,6))}**')
