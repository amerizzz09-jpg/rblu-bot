import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("บอทออนไลน์แล้ว:", bot.user)

    try:
        synced = await bot.tree.sync()
        print(f"ซิงค์คำสั่ง / สำเร็จ {len(synced)} คำสั่ง")
    except Exception as e:
        print("เกิดข้อผิดพลาดตอนซิงค์คำสั่ง:", e)

# ---- ตัวอย่างคำสั่ง /ping ----
@bot.tree.command(name="ping", description="ทดสอบการทำงานของบอท")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong! 🩵")

bot.run(os.getenv("TOKEN"))