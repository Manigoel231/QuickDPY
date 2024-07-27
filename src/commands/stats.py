import discord
from discord.ext import commands
import psutil
import time
from datetime import datetime, timedelta

class StatsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.utcnow()

    @commands.command(name='stats', help='A command to show the detailed statistics of the bot')
    async def stats(self, ctx):
        current_time = datetime.utcnow()
        uptime = current_time - self.start_time
        memory = psutil.virtual_memory()
        ram_usage = f"{memory.percent}% used ({memory.used / (1024 ** 3):.2f} GB out of {memory.total / (1024 ** 3):.2f} GB)"
        cpu_usage = f"{psutil.cpu_percent(interval=1)}%"
        stats_message = (
            f"**Bot Uptime:** {str(uptime).split('.')[0]}\n"
            f"**RAM Usage:** {ram_usage}\n"
            f"**CPU Usage:** {cpu_usage}\n"
            f"**Memory Info:**\n"
            f"  Total: {memory.total / (1024 ** 3):.2f} GB\n"
            f"  Available: {memory.available / (1024 ** 3):.2f} GB\n"
            f"  Used: {memory.used / (1024 ** 3):.2f} GB"
        )
        await ctx.send(stats_message)

async def setup(bot):
    await bot.add_cog(StatsCommand(bot))
    print('[COMMAND] | Commands: "stats" has been added')