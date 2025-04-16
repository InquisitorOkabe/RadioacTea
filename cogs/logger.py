from discord.ext import commands
import time

class Logger(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = time.strftime('[%Y-%m-%d %H:%M.%S]', time.gmtime())
    

    @commands.command()
    async def session_create(self, ctx, filename): 
        # print(filename)
        with open(f'./logs/{filename}.log', 'w') as file:
            file.write(self.session)

async def setup(client):
    await client.add_cog(Logger(client))