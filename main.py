import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"บอทออนไลน์แล้ว: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"ซิงค์คำสั่ง / แล้ว {len(synced)} คำสั่ง")
    except Exception as e:
        print(e)

@bot.tree.command(name="ping", description="เช็คว่าบอทยังออนไลน์ไหม")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong! 🏓")

bot.run(os.getenv"TOKEN")
