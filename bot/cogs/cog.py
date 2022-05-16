from pkgutil import iter_modules
from discord.ext import commands

class Cogs(commands.Cog):
    """To manage load/unloading of Cogs."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def cog(self, ctx, cmd: str, cog: str):
        """List/Unload/Load Cogs
        -cog load *cog*
        -cog unload *cog*
        -cog list all
        """
        cogs_list = [i[1] for i in iter_modules([self.bot.dir])][1:]
        if cmd == 'load':
            if cog in cogs_list:
                if cog in [i.lower() for i in ctx.bot.cogs]:
                    self.bot.reload_extension(cog.lower())
                    await ctx.send(f'Reloaded **{cog}**.')
                else:
                    self.bot.load_extension(cog.lower())
                    await ctx.send(f'Loaded **{cog}**.')
            else:
                await ctx.send(f'Did not find **{cog}**.')
        elif cmd == 'unload':
            if cog in cogs_list:
                if cog in [i.lower() for i in ctx.bot.cogs if i.lower()]:
                    if cog != 'cogs':
                        self.bot.unload_extension(cog.lower())
                        await ctx.send(f'Unloaded **{cog}**.')
                    else:
                        await ctx.send(f"Can't do that **{ctx.author.name}**.")
                else:
                    await ctx.send(f'Cog **{cog}** is not loaded.')
            else:
                await ctx.send(f'Did not find **{cog}**.')
        else:
            resp = '__**Cogs:**__'
            on = [i.lower() for i in ctx.bot.cogs]
            resp += '\n**On:** '+', '.join(on)
            off = [i for i in cogs_list if i not in on]
            resp += '\n**Off:** '+', '.join(off)
            await ctx.send(resp)
