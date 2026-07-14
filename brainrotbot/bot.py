import os
import random
import discord
from discord.ext import commands

TOKEN = "MTUyNjU1MzUyMzQwNjI0NTg5OQ.G9K4ZF.6D8rzdWA4s7ImxMOwR0gVhHGWAdHyCXD9JwBoU"

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} が起動しました！")

@bot.tree.command(
    name="brainrot",
    description="ブレインロット画像をランダムで10枚表示"
)
async def brainrot(interaction: discord.Interaction):

    folder = "brainrot"

    files = [
        f for f in os.listdir(folder)
        if f.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))
    ]

    if len(files) == 0:
        await interaction.response.send_message("brainrotフォルダに画像がありません。")
        return

    count = min(10, len(files))
    selected = random.sample(files, count)

    attachments = [
        discord.File(os.path.join(folder, f))
        for f in selected
    ]

    await interaction.response.send_message(files=attachments)

bot.run(TOKEN)
