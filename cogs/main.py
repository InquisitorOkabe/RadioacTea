import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() # Событие
    async def on_ready(self):
        print('Верховный Корги пробудился!')

    @commands.command() # Команда
    async def wof(self, ctx):
        await ctx.send('-Гав!-')

def setup(client):
    client.add_cog(Main(client))
