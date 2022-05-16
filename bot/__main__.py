from os import environ, path
from discord.ext import commands
from discord.ext.commands import CommandNotFound


bot = commands.Bot(command_prefix='-', description="* Commands *")
bot.dir = path.dirname(path.realpath(__file__))

@bot.event
async def on_command_error(ctx, error):
    """Return error message"""
    if not isinstance(error, CommandNotFound):
        await ctx.send('**Error:** {}'.format(error))


bot.load_extension('cogs')
bot.load_extension('utopia')
bot.run(environ['TOKEN'])
