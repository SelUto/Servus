import subprocess
from discord.ext import commands


PIPE = subprocess.PIPE

class Git(commands.Cog):
    """Git commands."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def pull(self, ctx):
        """Git Pull"""
        process = subprocess.Popen(["git", "pull", "--ff-only"], stdout=PIPE, stderr=PIPE)
        stdoutput, stderroutput = process.communicate()
        await ctx.send(f"__**Results**__\n\n{stderroutput.decode()}\n{stdoutput.decode()}"[:2000])
