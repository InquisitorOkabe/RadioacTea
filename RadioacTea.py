import os
import sys
import discord
from discord.ext import commands
from config_secure import settings
from config_secure import users_whitelist
from config_secure import roles_whitelist

ansi = {
    'info' : '\033[1;36m',
    'cogs' : '\033[2;33m',
    'white' : '\033[2;37m',
    'gray' : '\033[1;30m',
    'blue' : '\033[1;34m',
}

a = {
    'i' : '\033[1;36m',
    'c' : '\033[2;33m',
    'w' : '\033[2;37m',
    'g' : '\033[1;30m',
    'b' : '\033[1;34m',
}

# Выдача прав или "намерений" боту.
intents = discord.Intents.all()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=settings['prefix'], intents=intents, application_id=settings['id'])
        self.last_cog = 'main'

    async def on_ready(self):
        print(f'{a['i']}# INFO: {a['b']}[RadioacTea] {a['g']}*Звуки Респиратора.*')
        print(f'{a['i']}# INFO: {a['c']}[Корги] {a['g']}Начало загрузки.')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await client.load_extension(f'cogs.{filename[:-3]}')
                print(f'{a['i']}# INFO: {a['c']}[Корги] {a['w']}"{filename[:-3]}" {a['g']}загружен.')
        print(f'{a['i']}# INFO: {a['c']}[Корги] {a['g']}Загрузка завершена.')
        print(f'{a['i']}# INFO: {a['b']}[RadioacTea] {a['g']}Отчёт окончен.')
    pass

client = MyBot()



# Команда выключения бота.
@client.command()
async def exit(ctx):
    if ctx.author.id in users_whitelist: # Проверка доступа.
        await ctx.send(f'```Ручное отключение.```')
        await client.close()
        print(f'{a['i']}# INFO: {a['w']}Бот выключен пользователем {a['g']}{ctx.author.name}({ctx.author.id})')
    else:
        await ctx.send(f'```Ошибка доступа. [Уровни]: Белый.```')


# Команда загрузки Cogs.
@client.command()
async def load(ctx, extension=None):
    # Сверка прав.
    if ctx.author.roles or ctx.author.id in users_whitelist or roles_whitelist:
        try:
            # Если функция вызвана без аргумента - брать значение по умолчанию.
            extension = extension if extension != None else client.last_cog
            await client.load_extension(f'cogs.{extension}')
            client.last_cog = extension # Обновить значение по умолчанию.
            await ctx.send(f'```[{extension}] Корги: Прибежал.```')
        except Exception: # Детальный вывод ошибки, если функцию вызвал разработчик.
            if ctx.author.id in users_whitelist:
                # Разбираем на три части ошибку.
                exc_type, exc_obj, exc_tb = sys.exc_info()
                # Выводим красивое окно текста с заголовком.
                embed = discord.Embed(
                    title = exc_type.__name__,
                    description = str(exc_obj),
                    color = 0x1abc9c
                    )
                await ctx.send(embed = embed)
            else: # Простое сообщение об ошибке, если функцию вызвал рядовой пользователь.
                await ctx.send(f'```Ошибка.```')
    else:
        await ctx.send(f'```Ошибка доступа. [Уровни]: Белый, Корги.```')


# Команда выгрузки Cogs.
@client.command()
async def unload(ctx, extension=None):
    # Сверка прав.
    if ctx.author.roles or ctx.author.id in users_whitelist or roles_whitelist:
        try:
            # Если функция вызвана без аргумента - брать значение по умолчанию.
            extension = extension if extension != None else client.last_cog
            await client.unload_extension(f'cogs.{extension}')
            client.last_cog = extension # Обновить значение по умолчанию.
            await ctx.send(f'```[{extension}] Корги: Убежал.```')
        except Exception: # Детальный вывод ошибки, если функцию вызвал разработчик.
            if ctx.author.id in users_whitelist:
                # Разбираем на три части ошибку.
                exc_type, exc_obj, exc_tb = sys.exc_info()
                # Выводим красивое окно текста с заголовком.
                embed = discord.Embed(
                    title = exc_type.__name__,
                    description = str(exc_obj),
                    color = 0x1abc9c
                    )
                await ctx.send(embed = embed)
            else: # Простое сообщение об ошибке, если функцию вызвал рядовой пользователь.
                await ctx.send(f'```Ошибка.```')
    else:
        await ctx.send(f'```Ошибка доступа. [Уровни]: Белый, Корги.```')


# Команда перезагрузки Cogs.
@client.command()
async def reload(ctx, extension=None):
    # Сверка прав.
    if ctx.author.roles or ctx.author.id in users_whitelist or roles_whitelist:
        try:
            # Если функция вызвана без аргумента - брать значение по умолчанию.
            extension = extension if extension != None else client.last_cog
            await client.unload_extension(f'cogs.{extension}')
            await client.load_extension(f'cogs.{extension}')
            client.last_cog = extension # Обновить значение по умолчанию.
            await ctx.send(f'```[{extension}] Корги: Разворот на 360.```')
        except Exception: # Детальный вывод ошибки, если функцию вызвал разработчик.
            if ctx.author.id in users_whitelist:
                # Разбираем на три части ошибку.
                exc_type, exc_obj, exc_tb = sys.exc_info()
                # Выводим красивое окно текста с заголовком.
                embed = discord.Embed(
                    title = exc_type.__name__,
                    description = str(exc_obj),
                    color = 0x1abc9c
                    )
                await ctx.send(embed = embed)
            else: # Простое сообщение об ошибке, если функцию вызвал рядовой пользователь.
                await ctx.send(f'```Ошибка.```')
    else:
        await ctx.send(f'```Ошибка доступа. [Уровни]: Белый, Корги.```')


# Выводит список всех подключенных в данный момент Корги.
@client.command()
async def coglist(ctx):
    await ctx.send(f'```Имена всех Корги: {', '.join(client.cogs.keys())}.```')


# Команда перезапуска бота на уровне скрипта.
@client.command()
async def restart(ctx):
    # Сверка прав.
    if ctx.author.id in users_whitelist:
        print(f'{a['i']}# INFO: {a['b']}[RadioacTea] {a['g']}Ручная перезагрузка.')
        await ctx.send(f'```Перезагрузка по запросу {ctx.author.name}({ctx.author.id})```')
        # python = sys.executable # Получение пути к самому себе.
        # os.execl(python, python, * sys.argv) # Запуск скрипта, по пути, с аргументами.
        await client.close() # Закрыть бота.
        os.execl('[Start].bat', * sys.argv) # Запуск батника бота.
    else:
        await ctx.send('Ошибка прав доступа. [Уровни]: Белый.')
# --------- Test Zone Start ---------



# --------- Test Zone End ---------


# Не забыть, что оно вообще существует.
# embed = discord.Embed(
#     title = 'Перезапуск бота',
#     description = f'**Здраствуйте {ctx.author.mention}! Вы как разработчик бота BOT перезапустили его!**',
#     color = 0x1abc9c
#     )
# await ctx.send(embed = embed)


# --- End ---

client.run(settings['token'])