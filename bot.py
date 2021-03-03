#Knihovny:
import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord.voice_client import VoiceClient
import random
import asyncio
from time import sleep

#Ověrění
def is_it_me(ctx):
    return ctx.author.id == 710059910783697026

#Spuštění bota:
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)
client.remove_command("help")
token = ("ODExNjE2MDc4MTY5MjQzNjQ5.YC0yYA.Q-QRXESdu3MNpYKra89HjGSRYV0")

@client.event
async def on_ready():
    print("Jsem online!!!")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("si na serveru"))
   
#help
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.set_author(name="   ---------------  Help  ---------------  ")
    embed.add_field(name=".rozhovor", value="Odpoví na položenou otázku", inline=False)
    embed.add_field(name=".mampravdu", value="Odpoví Ano/Ne", inline=False)
    embed.add_field(name=".cislo", value="Vygeneruje random číslo 0-9", inline=False)
    embed.add_field(name=".úklid (počet)", value="vymaže zprávy", inline=False)

    await ctx.send(embed=embed)

#Připojení/Odpojení člověka:
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='hlavní-chat')
    await channel.send(f'Vítej {member.mention}! Kdyby jsi potřeboval pomoci můžeš dát ".help"!, nebo napsat do Supportu rádi ti pomůžeme...')
##    user = member
##    role = discord.utils.get(guild.roles, name="Neověřeno!")
##    await user.add_roles(role)

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='hlavní-chat')
    await channel.send(f'Člen {member.mention} nás opustil. :sob:')

##################################   příkazy pro členy   ######################################                   

#.rozhovor
@client.command()
async def rozhovor(ctx, *, question):
    seznam1 = ["Dobrý",
                 "Dobře ty",
                 "Mám se dobře",
                 "Jsi borec",
                 "Nevim",
                 "Super",
                 ":joy:",
                 "Juj"]
    await ctx.send(f"Otázka: {question}\nOdpověď: {random.choice(seznam1)}")


#.mampravdu
@client.command()
async def mampravdu(ctx, *, question):
    seznam1 = ["Možná",
                 "Ano",
                 "Ano",
                 "Ano",
                 "Ne",
                 "Ne",
                 "Ne"]
    await ctx.send(f"Otázka: {question}\nOdpověď: {random.choice(seznam1)}")

#.cislo
@client.command()
async def cislo(ctx):
    cisla = [    "1",
                 "2",
                 "3",
                 "4",
                 "5",
                 "6",
                 "7",
                 "8",
                 "9",
                 "0"]
    await ctx.send(f"{random.choice(cisla)}")

#.úklid
@client.command()
async def úklid(ctx, amount=4):
    await ctx.channel.purge(limit=amount)

###############################   správa serveru   ###############################################

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


#Vytvoř/smaž textový kanál
@client.command()
async def ahoj(ctx):
    guild = ctx.guild
    username = ctx.message.author.name
    his_name = get(guild.members, name=username)
    name = 'Příkazy pro boty'
    category = discord.utils.get(ctx.guild.categories, name=name)
    channel = await ctx.guild.create_text_channel(username, category=category)
    await channel.set_permissions(guild.default_role, view_channel=False, send_messages=False)
    await channel.set_permissions(guild.me, view_channel=True, send_messages=True)
    await channel.set_permissions(his_name, view_channel=True, send_messages=True)
    user = ctx.message.author
    role = discord.utils.get(guild.roles, name="Dřevo")
    await user.add_roles(role)
    user = ctx.message.author
    role = discord.utils.get(guild.roles, name="Neověřeno!")
    await user.remove_roles(role)
    await ctx.channel.purge(limit=1)

@client.command()
@commands.check(is_it_me)
async def delete(ctx, channel: discord.TextChannel):
    await channel.delete()


#Klient:
client.run(token)














