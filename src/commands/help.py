import discord
from discord.ext import commands

class HelpCmd(commands.HelpCommand):
    def get_ending_note(self):
        return "Use `!help <command>` for more information on a specific command."

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", description="List of all commands", color=0x00ff00)
        for cog, commands in mapping.items():
            if cog:
                command_list = [f"`{command.name}`: {command.short_doc}" for command in commands if not command.hidden]
                if command_list:
                    embed.add_field(name=cog.qualified_name, value='\n'.join(command_list), inline=False)
        await self.context.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=f"Help for `{command.name}`", description=command.description or "No description", color=0x00ff00)
        embed.add_field(name="Usage", value=command.usage or "No usage", inline=False)
        await self.context.send(embed=embed)

async def setup(bot):
    bot.help_command = HelpCmd()
    print('[COMMAND] | Commands: "help" has been added')