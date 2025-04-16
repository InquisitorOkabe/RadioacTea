from discord.ext import commands

class Pet(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Команда получает данные о пользователе из БД.
    # @commands.command()
    # async def check(ctx):
    #     # Мы должны по ID пользователя выдавать ему все данные о нём, если они есть.
    #     pass


    # Команда создания аккаунта на основе ID. Имя аккаунта вводится вручную.
    @commands.command()
    async def account_create(self, ctx, name):
        try:
            await ctx.send(f'```Создан аккаунт под именем [{name}] и привязан к вашему ID.```')
        except Exception:
            await ctx.send('```Техническая неполадка. Одумайтесь.```')
        pass


async def setup(client):
    await client.add_cog(Pet(client))