from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='Testing command, just to get the bot response')
    async def ping(self, ctx):
        await ctx.send('Pong!')

async def setup(bot):
    await bot.add_cog(PingCommand(bot))
    print('[COMMAND] | Commands: "ping" has been added')