bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="/add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="/multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="/greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="/cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="/info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="/help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)
