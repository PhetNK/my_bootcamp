import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

@bot.command()
async def info(ctx):
    data = discord.Embed(
        title="Sensor infomation",
        color=discord.Color.green()
    )

    data.add_field(name="Author" ,value=ctx.author.name ,inline=False)
    data.add_field(name="Server", value=ctx.guild, inline=False)
   
    data.set_footer(text="Bot Version 1.0")
    await ctx.send (embed=data)

@bot.command()
async def sensor(ctx,sensor_id: str):
    data = discord.Embed(
        title="🌡️ IoT Sensor Status",
        description="Real-time sensor data",
        color=discord.Color.green()
    )

    data.add_field(name="Device:",value=sensor_id,inline=False)
    data.add_field(name="Temperature" ,value="37.5 ํC" ,inline=True)
    data.add_field(name="Humidity", value="80%", inline=True)
   
    data.set_footer(text="Last update just now")
    await ctx.send (embed=data)

@bot.command()
async def alert(ctx,*,message: str):
    data = discord.Embed(
        title="ALERT",
        color=discord.Color.red(),
        timestamp=discord.utils.utcnow()
    )
    data.add_field(name="ALERT",value=message)
    data.set_footer(text="Alert at")
    await ctx.send (embed=data)


bot.run(TOKEN)