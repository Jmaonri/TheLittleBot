import discord
from discord.ext.commands import bot
from discord.ext import commands
from Token import token #imports Token.py which holds the bot token
import asyncio
import time
import twitch
from twitch import TwitchClient
import twitchio
from twitchio import commands as tcommands
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

#Startup Log
@client.event
async def on_ready():
    print(f"{client.user.name} is online and running")
    print('------')
    print("Log:\n")
    #Set the 'playing' status as the set string
    await client.change_presence(game=discord.Game(name='!Commands | !Github',  type = 1, url = 'https://www.twitch.tv/thelittledude_ld'))
 
#List of Awooo images
awooList = list(range(1, 18))
awooList[1] = "http://i.imgur.com/0nk3PVL.gif"
awooList[2] = "https://i.kym-cdn.com/entries/icons/original/000/017/280/e29.jpg"
awooList[3] = "https://pm1.narvii.com/6305/c7d8b91c654926212369dd7ad3aba76ba9fd9fc1_hq.jpg"
awooList[4] = "https://i1.kym-cdn.com/photos/images/newsfeed/000/910/236/1aa.gif"
awooList[5] = "https://forum.treeofsavior.com/uploads/default/original/3X/6/6/66884ea5d35c290a90f8e18dcad5763c14406b10.jpg"
awooList[6] = "https://i.redditmedia.com/F5qfZrFB_POv16QcUbeF6MmGXsz-tq1kpVXGO88cY6I.jpg?s=964624bcec5c41814e2051e0b48ae4f1"
awooList[7] = "https://lh3.googleusercontent.com/1jJlpBXasFKXgmGfujEnc9YpX3Fg_bUcnfeumb-_tShG5g1ryhmWHc90jYQ-f_SY58gkRogZ=w640-h360-p-rw"
awooList[8] = "https://img.fireden.net/a/image/1491/67/1491674057151.jpg"
awooList[9] = "https://img.4plebs.org/boards/s4s/image/1399/57/1399571113850.gif"
awooList[10] = "https://linustechtips.com/main/uploads/monthly_2018_05/awooo.thumb.png.d7d1bc01d8ed1d08c3f16f47f8cf5748.png"
awooList[11] = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8Fb8ohwkxBw8d-IxA20GYCl0PnCrYUTIYsGrkvAWsCNY-i1LB"
awooList[12] = "https://cdn.4archive.org/img/H0DP5BGm.jpg"
awooList[13] = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1QD9QGdqEId8uRRc3I8pzIM07QszYs2OiNK1RZ4NUquf-lp39Dw"
awooList[14] = "https://2static1.fjcdn.com/comments/Anonymous+roll+picture+searched+awooo+_3d6ebc1afdcf66d520593f323c34bb00.jpg"
awooList[15] = "https://ih1.redbubble.net/image.500965719.2653/st%2Csmall%2C215x235-pad%2C210x230%2Cf8f8f8.lite-1u1.jpg"
awooList[16] = "https://cdn.awwni.me/rhkb.png"

@client.event
async def on_message(message):
    if message.content.lower().startswith('!commands'):
        await client.send_message(message.channel, "```\nHere are all the commands:\n\n!Github - Link to the github of TheLittleBot\n!Awoo - Awooo?\n!Twitch - Sends link to TheLittleDude's Twitch channel```")
    if message.content.lower().startswith('ryan pls'):
        await client.send_message(message.channel, "Yeah shut the fuck up Ryan")
    if message.content.lower().startswith('!twitch'):
        await client.send_message(message.channel, "Here is TheLittleDude's Twitch:\nhttps://twitch.tv/thelittledude_ld")
    if message.content.lower().startswith('!awoo'):
        Embed = discord.Embed(title = "**~Awooo**")
        Embed.set_image(url = awooList[random.randint(1, 16)])
        await client.send_message(message.channel, embed = Embed)
    if message.content.lower().startswith('!github'):
        await client.send_message(message.channel, "https://github.com/Jmaonri/TheLittleBot")
    if message.content.lower().startswith('gay'):
        await client.send_message(message.channel, "<@!242378170534199306> You're being summoned")
    if message.content.lower().startswith('big gay'):
        await client.send_message(message.channel, "<@!242378170534199306> You're being summoned")

#Bot token goes here
client.run(token) #Opens Token.py and draws the token variable "client.run(file name, variable in file)"
