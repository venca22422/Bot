#Knihovny:
import discord
from discord.ext import commands, tasks
from discord.utils import get
import random


#Spuštění bota:
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot online!")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("si na serveru"))


#help
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name="Help")
    embed.add_field(name=".otázka", value="Odpoví na položenou otázku", inline=False)
    embed.add_field(name=".úklid (počet)", value="vymaže zprávy", inline=False)

    await ctx.send(embed=embed)

#Připojení/Odpojení člověka:
@client.event
async def on_member_join(ctx, member):
    await ctx.send("Ahoj {member}, vítáme tě u nás na serveru! :grin:")

@client.event
async def on_member_remove(ctx, member):
    await ctx.send("Člen {member} nás opustil. :sob:")

#Ověrění
def is_it_me(ctx):
    return ctx.author.id == 710059910783697026

#Kommandy:
#.otázka
@client.command()
async def otázka(ctx, *, question):
    responses = ["Super",
                 "Super",
                 "A dál?",
                 "Hustý",
                 "Hustý",
                 "Mám se dobře",
                 "Mám se dobře",
                 "Ano",
                 "Ano",
                 "Ano",
                 "Ne",
                 "Ne",
                 "Ne"]
    await ctx.send(f"Otázka: {question}\nOdpověď: {random.choice(responses)}")

#.úklid
@client.command()
async def úklid(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

#.kick
@client.command()
@commands.check(is_it_me)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} byl kicknut.")

#.ban
@client.command()
@commands.check(is_it_me)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} byl zabanován.")

#.unban
@client.command()
@commands.check(is_it_me)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanován {user.mention}")
            return


@client.command()
async def vytvořkanál(ctx, channelName):
    guild = ctx.guild
    await guild.create_text_channel(name="{}".format(channelName))

@client.command()
async def smažkanál(ctx, channel: discord.TextChannel):
    await channel.delete()

###.připoj
##@client.command(pass_content=True)
##async def připoj (ctx):
##    channel = ctx.message.author.voice.channel
##    if not channel:
##        await ctx.send("You are not connected to a voice channel")
##        return
##    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
##    if voice and voice.is_connected():
##        await voice.move_to(channel)
##    else:
##        voice = await channel.connect()
##
###.odpoj
##@client.command(pass_context = True)
##async def odpoj(ctx):
##    channel = ctx.message.author.voice.channel
##    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
##    if voice and voice.is_connected():
##        await voice.disconnect()
##    else:
##        await voice.disconnect()
##        await ctx.send("Nejsem v hlasovém kanálu!")
##
##
###.pause
##@client.command()
##async def pause(ctx):
##    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
##    voice.pause()
##
###.pokračuj
##@client.command()
##async def pokračuj(ctx):
##    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
##    if voice.is_paused():
##        voice.resume()
##    else:
##        await ctx.send("Nic není pauznuté!")
##
###.stop
##@client.command()
##async def stop(ctx):
##    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
##    if voice.is_connected():
##        voice.stop
##    else:
##        await ctx.send("Nepřehrávám audio!")

       
#Klient:
client.run("ODExMjQzMjM3MTkyMzY4MjE5.YCvXIw.YcBO0s58tlbq4irKDzG32IwEwY8")















