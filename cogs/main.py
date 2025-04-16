from discord.ext import commands
from config_secure import users_whitelist

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wof(self, ctx):
        await ctx.send(f'```-Вуф!-```')

    # Удаление сообщений в чате, где введена команда.
    @commands.command()
    async def clear(self, ctx, limit='10'): # Стирает N сообщений, по умончалию - 10. Меееееедленно.
        if ctx.author.id in users_whitelist:
            if limit == 'all':
                # ToDo:
                # Проверить иные методы удаления сообщений на скорость. Например: [delete_message].
                await ctx.channel.purge() # Стереть к хуям весь канал. (Примерно 3 сообщения в секунду.)
                await ctx.send(f'```Геноцид завершён. Число жертв: ДА!```')
            else:
                await ctx.channel.purge(limit=int(limit)+1)
                await ctx.send(f'```Геноцид завершён. Число жертв: {limit}```')
        else:
            await ctx.send('```Ошибка доступа. [Уровни]: Белый.```')


async def setup(client):
    await client.add_cog(Main(client))