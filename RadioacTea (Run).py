import discord
from discord.ext import commands
# from discord_components import DiscordComponents, Button, ButtonStyle
from config import settings
from config import rules_whitelist
# import requests
import os
# import asyncio
# import random

client = commands.Bot(command_prefix = settings['prefix'])
token = settings['token']
# --- Заметки ---
# client.get_user(id) - получает класс пользователя.
# client.get_emoji(id) - получить смайлик, который можно впихнуть в строку.

# rules_whitelist = [ # User ID:
#                    ******************, # Окабэ
#                    ******************, # Грейвз
#                    ******************, # Коняга
#                    ]

@client.event
async def on_ready():
    print('*Звуки Респиратора*')

@client.command()
async def exit(ctx):
    if ctx.author.id in rules_whitelist:
        await ctx.send('Бот ~~делает харакири~~ выключается.')
        await client.close()
        # await client.logout()
    else:
        await ctx.send('Вы не Окабэ. Идите нахер.')

@client.command()
async def load(ctx, extension):
    role = ctx.guild.get_role(877240294393938011)
    if role in ctx.author.roles or ctx.author.id in rules_whitelist:
        try:
            client.load_extension(f'cogs.{extension}')
            await ctx.send(f'"{extension}" Корги: Прибежал.')
        except Exception:
            await ctx.send('Ни одного Корги так не зовут!')
    else:
        await ctx.send('Вы не Корги.')

@client.command()
async def unload(ctx, extension):
    role = ctx.guild.get_role(877240294393938011)
    if role in ctx.author.roles or ctx.author.id in rules_whitelist:
        try:
            client.unload_extension(f'cogs.{extension}')
            await ctx.send(f'"{extension}" Корги: Убежал.')
        except Exception:
            await ctx.send('Ни одного Корги так не зовут!')
    else:
        await ctx.send('Вы не Корги.')

@client.command()
async def reload(ctx, extension):
    role = ctx.guild.get_role(877240294393938011)
    if role in ctx.author.roles or ctx.author.id in rules_whitelist:
        try:
            client.unload_extension(f'cogs.{extension}')
            client.load_extension(f'cogs.{extension}')
            await ctx.send(f'"{extension}" Корги: Разворот на 360.')
        except Exception:
            await ctx.send('Ни одного Корги так не зовут!')
    else:
        await ctx.send('Вы не Корги.')

print('# info: --- Начинается загрузка Корги ---')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'# info: --- Cog "{filename[:-3]}" загружен ---')
print('# info: --- Все Корги загружены ---')
print('# info --- Загрузка прочих компонентов ---')
# DiscordComponents(client)
print('# load: DiscordComponents')
print('Бот активирован...')
print('Бот активирован...')
client.run(token)
