"""
Simple calendar bot for discord.
Send image and text on scheduled days.
Send current day's date.
"""

import discord, datetime
from discord.ext import commands

bot = commands.Bot("!")
itens = discord.Intents.all

# To see bot commands
@bot.command(name="commands")
async def send_date(ctx):
    response = "The calendar commands are: \n" \
               "!date (to see the current date) \n" \
               "!commands (to see the calendar commands)"
    response = str(response)
    await ctx.send(response)

# View the current day's date
@bot.command(name="date")
async def send_date(ctx):
    name = ctx.author.name
    date = datetime.datetime.now()
    response = f"Today's date is {date.month} {date.day} {date.year} " + name
    response = str(response)
    await ctx.send(response)
    
# Send image and text on scheduled days
@bot.event
async def on_ready():
    date_now = datetime.datetime.now()
    date_now = f"{date_now.day} {date_now.month} {date_now.year}"

    nat = datetime.datetime(2022, 4, 2)  # You can schedule dates here
    nat = f"{nat.month} {nat.day} {nat.year}"  # you can sort the dates according to the order you want
    if date_now == nat:
        embed = discord.Embed(title="Title",  # Send title
                              description="description",  # send description
                              color=0x8d27e6  # Adjust color
                              )
        ctx = bot.get_channel()  # Send ID from your Channel
        embed.set_image(url="your url link")  # Send url link
        await ctx.send(embed=embed)


bot.run("Your token here")
