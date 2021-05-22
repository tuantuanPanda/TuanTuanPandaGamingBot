import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='/', description='A bot that greets the user back.')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    @bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.cmmands()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

def new_func():
    new_var = new_func1()
    return new_var
/ python bot.py

- python nice_bot.py
Logged in as
my-nice-bot
845457702884605953

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    
    # 在这里提供关于您的信息
    embed.add_field(name="Author", value="<YOUR-USERNAME>")
    
    # 显示机器人所服务的数量。
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # 给用户提供一个链接来请求机器人接入他们的服务器
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)
    
    
