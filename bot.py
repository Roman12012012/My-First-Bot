import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

# Цены стендов
stands_cost = {
    "SPL": 5000, "TW": 5000, "SFI": 5000, "PH": 5000, "HP": 5000, "RHCP": 5000,
    "KQ": 5000, "KC": 5000, "SC": 5000, "TH": 5000, "AS": 5000, "WS": 5000,
    "SFR": 5000, "AN": 5000, "CD": 5000, "CR": 5000, "HG": 5000, "MR": 5000,
    "WA": 5000, "SPI": 5000, "BB": 5000, "MP": 5000, "SM": 5000, "TWAU": 5000,
    "D4C": 5000, "S & W": 5000, "T1": 5000, "GER": 6000, "KCR": 6000, "SCR": 6000,
    "KQBTD": 6000, "SPTW": 6000, "WR": 3000, "S&WGB": 12000, "T2": 15000,
    "T3": 16000, "T4": 46000, "D4CLT": 35000, "C-M": 7000, "MIH": 10000,
    "TWOH": 100000, "STW": 50000, "RHCPAU": 35000
}

# Названия стендов
stands_name = {
    "SPL": "Star Platinum", "TW": "The World", "SFI": "Sticky Fingers",
    "PH": "Purple Haze", "HP": "Hermit Purple", "RHCP": "Red Hot Chili Pepper",
    "KQ": "Killer Queen", "KC": "King Crimson", "SC": "Silver Chariot",
    "TH": "The Hand", "AS": "Aerosmith", "WS": "White Snake", "SW": "Soft & Wet",
    "AN": "Anubis", "CM": "C-Moon", "CR": "Cream", "HG": "Hierophant Green",
    "MIH": "Made in Heaven", "WA": "White Album", "SPI": "Six Pistols",
    "BB": "Bad Company", "SM": "Scary Monsters", "TWOH": "The World Over Heaven",
    "D4C": "Dirty Deeds Done Dirt Cheap", "TA1": "Tusk Act 1", "GER": "Gold Experience Requiem",
    "KCR": "King Crimson Requiem", "SCR": "Silver Chariot Requiem",
    "KQBTD": "Killer Queen Bites the Dust", "SPTW": "Star Platinum: The World",
    "WR": "Wether Report", "SWGB": "Soft & Wet: GB", "TA2": "Tusk Act 2",
    "TA3": "Tusk Act 3", "TA4": "Tusk Act 4", "D4CLT": "Dirty Deeds Done Dirt Cheap: Love Train",
    "SFR": "Stone Free", "RHCPAU": "Red Hot Chili Pepper Alternate Universe"
}

stands_id_ans = "\n".join(f"{k} - {v}" for k, v in stands_name.items())

@bot.command()
async def help(ctx):
    help_text = (
        "Вот список команд:\n"
        "/buy [стенд] - показывает цену указанного стенда\n"
        "/credit [число] - показывает сколько ты должен вернуть при возврате кредита\n"
        "/stands_id - показывает как разные стенды идентифицируются"
    )
    await ctx.channel.send(help_text)

@bot.command()
async def buy(ctx, stand):
    try:
        await ctx.channel.send(f'Стенд {stands_name[stand]} стоит {stands_cost[stand]}')
    except KeyError:
        await ctx.channel.send('Стенд не найден XD')

@bot.command()
async def stands_id(ctx):
    await ctx.channel.send(f'Вот все имена стендов:\n{stands_id_ans}')

procent = 0

@bot.command()
async def credit(ctx, n: int):
    await ctx.channel.send(f'Вы должны будете вернуть {n + n * procent}')

bot.run(TOKEN)
