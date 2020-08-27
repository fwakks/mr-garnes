import discord
import os
import random
import asyncio
import datetime
import json
import youtube_dl
import shutil
from discord.ext import commands
from discord.utils import get
from discord import Game


client = commands.Bot(command_prefix = '?')

players = {}


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with no child's feelings"))
    print('Mr. Garnes is online!')

@client.command()
async def guidance(ctx):
    await asyncio.sleep(1)
    member = ctx.author
    await ctx.send(f'Come to my office {member.mention}!')
    channel = ctx.author.voice.channel
    await asyncio.sleep(1)
    vc = await channel.connect()
    room = discord.Object(732245382691684444)
    await vc.move_to(room)
    await member.move_to(room)


@client.command(brief='?send @user')
async def send(ctx, user : discord.Member):
    await asyncio.sleep(1)
    channel = ctx.author.voice.channel
    await ctx.send(f"Like it or not {user.mention}, you're coming to my office now.")
    vc = await channel.connect()
    room = discord.Object(732245382691684444)
    await asyncio.sleep(1)
    await vc.move_to(room)
    member = user
    await member.move_to(room)

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command(brief='?iwonder [question]')
async def iwonder(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes – definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.'
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Do not count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def tardio(ctx, aliases=['Tardio']):
    responses = ['SIT DOWN!!! :angry: ',
                'STOP TALKING!!!',
                'IF YOU HAVE A PROBLEM WITH ME WE CAN TAKE IT TO MR. HUGHES!!!',
                '**RED**',
                '*"If you build it they will cum."*',
                '**STOP SAYING JOE ROGAN!!!** :angry: :joe_rogan: ',
                'ABUUUUUUUUUUU',
                'NAME, DATE, HOMEROOM, TOP RIGHT CORNER!!!',
                'AKSHAY GOT NEW SNEAKERS'
                ' AKSHAY GOT NEW SNEAKERS',
                '2 0 8 line *up!!*',
                "GUESS WHO'S BACK??? AKSHAY'S BACKSHAY!!! :partying_face:",
                ":musical_note: ***RED RED WIIIIIIIIIINNNNEEEE*** :musical_note:"
                '\nhttps://media.discordapp.net/attachments/689282153292234949/739355831723884554/image0.gif',
                'https://cdn.discordapp.com/attachments/485598975307677717/745882692238704740/L1dhaCuUQPJBZ2wt_A4D5L5AA-kFhfUH7Swazf-xOuYeNkFGTkwX28ntMYQN4u754lfAb657sap3CsmCrjUgHjiQ-xM8LaxSjKXD.png',
                'https://cdn.discordapp.com/attachments/485598975307677717/745883819038474280/image-asset.png',
                'https://cdn.discordapp.com/attachments/746411118972633112/748101240554127380/2018-10-08.png',
                'https://cdn.discordapp.com/attachments/746411118972633112/748210763646369802/image0.jpg']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def classic(ctx):
    responses = [ '6 8 9 ',
                  "Who's on first, What's on second, I Don't Know is on third",
                  "It’s not a screenshot if it doesn’t capture the whole screen",
                  'I am not your bro. And I will never BE your bro.',
                  'We have been doing this since the beginning of the *year!* - Daniel Monigle',
                  "Mabuti",
                  "Am I speaking Chinese?",
                  'PEM dat ass backwards',
                  'ACTUAL FACTUAL',
                  'DONKEYYYY',
                  '*Eighth Grade!!!*'
                  '*Hairline City*',
                  '**Coon**',
                  "Shut up Mr. Stewart's son",
                  "___***I KNOW YOU'RE NOT TALKING!!!***___",
                  "Is this an aux cable or an 'ayy you ex' cable?",
                  "Facts don't care about your feelings.",
                  ":musical_note: Rolling with the homies :musical_note:",
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573621232238622/the_saint.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573662223171687/no_means_yes.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573671312490576/no_game.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573685728051362/IMG_0433.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573694087299234/IMG_0434.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573722457702510/ED.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573736986640535/2018-10-16.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573847288447046/IMG_0435.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/746412033754529812/unknown.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747624897618116608/you_know_ms_freeman_had_to_do_it_to_em.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747633387371757628/2020-03-21.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747633478442418276/2020-03-21.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748225458264473732/4471773975408788150.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747635196785852467/31OcX3Epyh_PpKJ7CqSMIfaI11NPU9yTX1qsTIOY-CAkV7k9pLi9BGbX25vIWO14StnxxVQtUwovoEBEnT3giPZc0SBVJSMFsOcN.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747636571288633444/wut_1.gif',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747637626902675558/HufxzF9GgDonXbZdwACqWf-P0wEec9hZDvP_30wlDd81JnBRoEc-SlbvCP0yYnj0kViDrlpRNViXNsdVkiGx856_8D3Lm40HXvFd.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747637743177433108/LN66f6l9AP97tNEYb9Awkt8Byc4CNtUlBRM8pI-xE3KgtYDpnj_-oMgLNHpxUQwvojL5qReWS5nnKn7TVU8-6R4TMfguAOm9Rv4x.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747637934345420810/5lgCDEFkKVqusSJxz8vDdE2c-ZyIkHpDlNzVjTgKiHqoWbKlIGPbibGlmnW4Uei3oxBzD3nwVQAEXC9jPhwAJjEN0oXyxZGfOYuT.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639549966024804/ahhh_das_hot.PNG',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747642109489709116/2020-03-15_2.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747640381616947346/rap_god.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747640001331724388/stranger_danger.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639837959520306/peak_performance.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639785233055834/jon_is_a_school_shooter.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639702034841680/bruh_momento.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639672209014864/bouta_catch_these_hands.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747644203852627968/unknown.png',
                  "https://cdn.discordapp.com/attachments/746411118972633112/747644326183436375/2019-02-19_1.png",
                  'https://cdn.discordapp.com/attachments/746411118972633112/748210374402244718/2019-12-10.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748210672512401458/image0.jpg',
                  'https://streamable.com/322fyv',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748211198750883880/image0.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748212642862202960/2019-02-16.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748212965198528624/unknown.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748213126855524382/unknown.png',
                  'https://streamable.com/kf0q1b',
                  "https://streamable.com/8zasog"
                  'https://cdn.discordapp.com/attachments/746411118972633112/748218613017739344/2019-07-15.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748220215610835045/2019-10-05.png']
# These commands will be of every other quote of teachers or students from A1 that isn't tardio
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def funni(ctx):
    responses = ['https://cdn.discordapp.com/attachments/746411118972633112/747640095057641503/Dory.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747640128922714193/Drake_and_Jon.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747640151240343682/Friend_a_friend.jpg',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747640450533425172/ronald_basil.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747618595122577488/please_dont_take_the_kids.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747639023815884880/b3Cj-qTBLgF8lBS4EIeaXzsfNPdwcNDrvjIVzXBBnVQ7xWNad0tKf_YsgUCUJ_78nvkVFA9nT0bi8CXGUzOhKaRUPxIFp2HI7UtY.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747625833132458064/Finding_Luke.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747632686453227570/N_word_sayer_dies.png','https://cdn.discordapp.com/attachments/746411118972633112/747632686453227570/N_word_sayer_dies.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747627186776965150/xepqpwdiE4TSZJ_u60EYVEalmYL8GtnoA0lL9uEQDfKd1CdFBPKax5cz1bicvfLtGSc0WwhL5acgvHcbM1_uWmGJls4wnk5SuSpZ.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747642097116512396/2020-03-15_1.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747643076163666061/2019-06-21.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747643097202032650/2019-06-21_1.png',
                 'https://cdn.discordapp.com/attachments/746411118972633112/747643403319115856/2019-11-03.png',
                 'https://streamable.com/4y2k7m',
                 'https://streamable.com/ubgo5h']
# These are funni haha memes
    await ctx.send(f'{random.choice(responses)}')

@client.command(brief='quotes and images of mhadbhi himself')
async def bean27(ctx):
    responses = ['GOLDEN GOLDEN GOLDEN GOLDEN',
                 'BEANHEAD!!!',
                 'RAPTORS IN GAME 6',
                 "ALWAYS FINAGLING I SWEAR",
                 "https://cdn.discordapp.com/attachments/746411052132073623/748100540688498689/2018-10-08.png",
                 'https://cdn.discordapp.com/attachments/746411052132073623/747620495276376229/unknown.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/747620618748428348/unknown.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/747620653624066058/that_nayrootoh_show.jpg',
                 'https://cdn.discordapp.com/attachments/746411052132073623/747620705054752838/timmy_turner.jpg',
                 'https://cdn.discordapp.com/attachments/746411052132073623/747620900915904552/yin.jpg   '
                 'https://cdn.discordapp.com/attachments/746411052132073623/747620936793980968/yang.jpg',
                 'https://cdn.discordapp.com/attachments/746411052132073623/747633430702981172/2020-03-21.png'
                 'https://cdn.discordapp.com/attachments/746411052132073623/747638258430902294/8BwM0ZOniMw8r5AWBy0X3wxOHjhKywWztK1jPwesHXJbuX1Bf6_LAeCHHKfTpZqgxXf8nACy6kh1jXkLWmh2H6hH0mUnsiHCKg08.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/747638722706538667/9OAwTqiXU8c5-s4NNNlSLPDBH5RCk3HWwjtdCPZ-99dEjnVVg2k6iDmrR0hVoQA_6Q8hUew371-_jLDAeiUBWUl4J2U7-ApwoZFj.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/747653578679648416/2018-10-29_2.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/747653634581332079/2018-10-29_3.png',
                 'https://streamable.com/hlihom',
                 'https://streamable.com/y199z9',
                 'https://streamable.com/vo3ifn',
                 'https://cdn.discordapp.com/attachments/746411052132073623/748212006443548873/unknown.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/748212370240831488/unknown.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/748213272913903656/2019-02-19_3.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/748213399057334393/2019-02-19_4.png',
                 'https://cdn.discordapp.com/attachments/746411052132073623/748213525674983435/2019-02-19_5.png']
# These commands will be of all Amir's famous quotes
    await ctx.send(f'{random.choice(responses)}')

@client.command(brief='classic command but only images')
async def classimg(ctx):
    responses = ['https://cdn.discordapp.com/attachments/746411118972633112/747573621232238622/the_saint.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573662223171687/no_means_yes.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573671312490576/no_game.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573685728051362/IMG_0433.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573694087299234/IMG_0434.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573722457702510/ED.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573736986640535/2018-10-16.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747573847288447046/IMG_0435.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/746412033754529812/unknown.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747624897618116608/you_know_ms_freeman_had_to_do_it_to_em.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747633387371757628/2020-03-21.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747633478442418276/2020-03-21.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748225458264473732/4471773975408788150.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747635196785852467/31OcX3Epyh_PpKJ7CqSMIfaI11NPU9yTX1qsTIOY-CAkV7k9pLi9BGbX25vIWO14StnxxVQtUwovoEBEnT3giPZc0SBVJSMFsOcN.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747636571288633444/wut_1.gif',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747637626902675558/HufxzF9GgDonXbZdwACqWf-P0wEec9hZDvP_30wlDd81JnBRoEc-SlbvCP0yYnj0kViDrlpRNViXNsdVkiGx856_8D3Lm40HXvFd.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747637743177433108/LN66f6l9AP97tNEYb9Awkt8Byc4CNtUlBRM8pI-xE3KgtYDpnj_-oMgLNHpxUQwvojL5qReWS5nnKn7TVU8-6R4TMfguAOm9Rv4x.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747637934345420810/5lgCDEFkKVqusSJxz8vDdE2c-ZyIkHpDlNzVjTgKiHqoWbKlIGPbibGlmnW4Uei3oxBzD3nwVQAEXC9jPhwAJjEN0oXyxZGfOYuT.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639549966024804/ahhh_das_hot.PNG',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747642109489709116/2020-03-15_2.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747640381616947346/rap_god.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747640001331724388/stranger_danger.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639837959520306/peak_performance.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639785233055834/jon_is_a_school_shooter.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639702034841680/bruh_momento.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747639672209014864/bouta_catch_these_hands.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/747644203852627968/unknown.png',
                  "https://cdn.discordapp.com/attachments/746411118972633112/747644326183436375/2019-02-19_1.png",
                  'https://cdn.discordapp.com/attachments/746411118972633112/748210374402244718/2019-12-10.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748210672512401458/image0.jpg',
                  'https://streamable.com/322fyv',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748211198750883880/image0.jpg',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748212642862202960/2019-02-16.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748212965198528624/unknown.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748213126855524382/unknown.png',
                  'https://streamable.com/kf0q1b',
                  "https://streamable.com/8zasog"
                  'https://cdn.discordapp.com/attachments/746411118972633112/748218613017739344/2019-07-15.png',
                  'https://cdn.discordapp.com/attachments/746411118972633112/748220215610835045/2019-10-05.png']
# This is classic but only images
    await ctx.send(f'{random.choice(responses)}')

@client.command(brief='classic command but only text')
async def classtext(ctx):
    responses = ['6 8 9 ',
                  "Who's on first, What's on second, I Don't Know is on third",
                  "It’s not a screenshot if it doesn’t capture the whole screen",
                  'I am not your bro. And I will never BE your bro.',
                  'We have been doing this since the beginning of the *year!* - Daniel Monigle',
                  "Mabuti",
                  "Am I speaking Chinese?",
                  'PEM dat ass backwards',
                  'ACTUAL FACTUAL',
                  'DONKEYYYY',
                  '*Eighth Grade!!!*'
                  '*Hairline City*',
                  '**Coon**',
                  "Shut up Mr. Stewart's son",
                  "___***I KNOW YOU'RE NOT TALKING!!!***___",
                  "Is this an aux cable or an 'ayy you ex' cable?",
                  "Facts don't care about your feelings.",
                  ":musical_note: Rolling with the homies :musical_note:"]
# This is classic but only text
    await ctx.send(f'{random.choice(responses)}')


@client.command(brief='The Holy Scripture of Mr.Oussalem')
async def btb(ctx):
    responses = [ "Allen, you have a negative point Oussalem 1:1",
                  "I’m going to start giving negative grade  Oussalem 1:2",
                  "I have about an E+ in Math Oussalem 1:3",
                  "Use your mind power  Oussalem 1:4",
                  "Don’t Ask, anyone ask, I’m the teacher; Karla’s the teacher too  Oussalem 1:5",
                  "Oh yes, then no Oussalem 1:6",
                  "I will send you over the class   Oussalem 1:7",
                  "If I pick you, then I give full grade Oussalem 1:8",
                  "Sometimes I cancel participation if they didn’t go up on the board Oussalem 1:9",
                  "His hand is bleeding"
                   '\nGo away'
                   '\nBut it’s bleeding'
                   "\nI’m trying to go group by group, I’ll answer your question later"
                   '\nCome here and just see him'
                   "\nNo     Oussalem 1:10",
                   "Guys, I may take all of your grades!  Oussalem 1:11",
                   "If you misbehave, you’ll have no grades in my class  Oussalem 1:12",
                   "We are doing Algebra 1 by learning the geometry  Oussalem 1:13",
                   "Enaiy  Oussalem 1:14",
                   "I’ll be the daughter of my daughter  Oussalem 1:15",
                   "I’m about to distributive property on group number 1   Oussalem 1:16",
                   "I looked outside and distributed you guys- Oussalem 1:17",
                   "(Chinese kid asks a question)"
                   "\nAm I speaking Chinese or Spanish?  Oussalem 1:18",
                   "I always ask, it’s never you who questions  Oussalem 1:19",
                   "I wait for you to ask, but you don’t  Oussalem 1:20",
                   "Karla, we go step-by-step, stop going step-by-step  Oussalem 1:21",
                   "We answer when we follow directions  Oussalem 1:22"
                   "If you misbehave, then you’ll have me all week long Oussalem 1:23",
                   "No play cards, Ashton, go play on the computer   Oussalem 1:24",
                   "I’ll cancel the field trip if you don’t do extra credit   Oussalem 1:25",
                   "(You’re a hypocrite)"
                   "\nStop telling me what to do  Oussalem 1:26",
                   "I’m not teaching, it’s not my period, but do this extra credit now Oussalem 1:27",
                   "Don’t teach me what I’m already doing  Oussalem 1:28",
                   "If you listen, just listening, you don’t have to pay attention to the video. Be Quiet"
                   "\nOussalem 1:29",
                   "(No one is paying attention to the video)"
                   "\nYou no listen to video and then say that everyone’s no listen to video. Stop interfering with my job, you always interfered with my job. Don’t listen, it’s everyday you do this to me. Do you want to stand up and teach? No? Why must you always take over my position. How is it that I don’t teach now?!   Oussalem 1:30",
                   "Chesshta move to the back if you have trouble seeing things Oussalem 1:31",
                   "I didn’t know I had kids of two years old until now  Oussalem 1:32",
                   "It’s 5 days until June Oussalem 1:33",
                   "My calendar says it is 4-7 days until June   Oussalem 1:34",
                   "This class is the worst one   Oussalem 1:35",
                   "If you are quiet, then I’ll teach you a disaster  Oussalem 1:36",
                   "This is in-inacceptable   Oussalem 1:37"
                   "If you don’t hand in progress reports, then it’ll be homework  Oussalem 1:38",
                   "Sign it by this week and tomorrow  Oussalem 1:39",
                   "If you behave poorly, then I give quiz and test, the test is on Tuesday  Oussalem 1:40",
                   "Want me to go fast and do a lesson?  Oussalem 1:41",
                   "I think we don’t need to ask questions in this class Oussalem 1:42",
                   "Somehow add zero over here  Oussalem 1:43",
                   "Solution means something like water or alcohol  Oussalem 1:44",
                   "10% divide by eggs   Oussalem 1:45",
                   "The width of the water  Oussalem 1:46",
                   "You is failing test if you wasting time  Oussalem  1:47",
                   "It was on Tuesday. You is going too far  Oussalem 1:48",
                   "First minus 2, then minus 4, afterwards minus 10, then I take zero"
                   "\n(The grade is -18?!) Oussalem 1:49",
                   "Find a circumference of rectangle  Oussalem 2:1",
                   "If you misbehave. Then this is your last day here   Oussalem 2:2",
                   "(This month is immigrant heritage month)"
                   "\n(We must celebrate it with Mr. Oussalem!)"
                   "What did you just say to me?! Come over here, I am real citizen from Algerian, am no immigrant  Oussalem 2:3",
                   '(Today is national say something nice day, and you are a nice teacher)'
                   "\nWhy did you say I am a good teacher  Oussalem 2:4",
                   "I see like you know none of you follow directions, I won't bring you next time here if you don't be quiet. Oussalem 2:5",
                   "No radish, just math  Oussalem 2:6",
                   "It’s 10:10. So period is 5 more minutes. No more radish is not wise Oussalem 2:7",
                   "If you’re happy now, you’ll be very miserable later on Oussalem 2:8",
                   "(You can’t do that)"
                   "\nTake a seat"
                   "\n(I am seating already) Mr.Oussalem 2:9",
                   "This is my problem, but yet you ask for the problem   Oussalem 2:10",
                   "I grade some test, but you is grading   Oussalem 2:11",
                   "I’ll call your parents if you say that again"
                   "\n(But I want to know what kind of class this is)"
                   "\nCalculator   Oussalem 2:12",
                   "(How old is your son and daughter)"
                   "\nHuh?  Oussalem 2:13",
                   "I don’t like questions"
                   '\n(But answering them is your job)'
                   "\nLeave me alone! Do the warm up!   Oussalem 2:14",
                   "I’ll take your notebook from last year because of this Oussalem 2:15",
                   "Why you do this to Mr.Oussalem; poor man. Stop telling him I know this I know this I know this because this is something you did not learn  -Ms.Elmahi 2:16",
                   "No,No, this you know it know it, the slope intercept. You are smart but constantly take advantage.” -Ms.Elmahi 2:17",
                   "There is no bathroom period. Oussalem 2:18",
                   "Hands down and detention   Oussalem 2:19",
                   "Take a quiz but ask questions right questions no please be quiet I’m just a teachers Oussalem 2:20",
                   "Whole group minus 4 now!"
                   "\n(Well you’re being negative stupid)  Oussalem 2:21",
                   "Don’t ask the questions to friend questions  Oussalem 2:22",
                   "Negative 8 grade or quiz now   Oussalem 2:23",
                   "I take all notebooks then textbooks afterwards  Oussalem 2:24",
                   "(I pledge allegiance to the fla-)"
                   "\nWhy is everyone standing up and talking   Oussalem 2:25",
                   "To prepare for Algebra 2, we must do the Algebra 1 now  Oussalem 2:26",
                   "You make me noise...while everyone else is talking  Oussalem 2:27",
                   "There is 15 days of school left"
                   '\n(Actually, our last day is the 22nd)'
                   "\nStop this now you is arguing with me  Oussalem 2:28",
                   "You gaving me deception. I don’t need this stupid behavior   - Mr.Oussalem 2:29",
                   "(Sandra laughs heartily at Mr.Oussalem)"
                   "\nDo you laugh on the street?!?!"
                   '\n(Yes)'
                   "\nDo you laugh in your house!?"
                   '\n(Yup)'
                   "\nNegative grade  Oussalem 2:30",
                   "\nStand up"
                   '\n(No)'
                   "\nStand up"
                   '\n(Nope)'
                   "\nStand up"
                   '\n(Absolutely not)'
                   "\nSTAND UP"
                   '\n(Not doing it)'
                   "\nI’m the security"
                   '\n(No your not)'
                   "\nI’ll call them then"
                   '\n(You’ll be hearing from my mother)'
                   "\nWill do   Oussalem 2:31",
                   '(You are constantly pointing out all of the hispanic and black kids when they are innocent and respect you)'
                   "\nWhatever, just do your work and else  Oussalem 2:32",
                   "(You constantly say whether and not we right and wrong and that we are disrespecting you, but you never give us an ounce of respect)"
                   "\nNegative 1 in addition to 2 Oussalem 2:33",
                   "(You are always contradicting yoursel-)"
                   "\nRicardo, didn’t I just say no question me at end of class?! Oussalem 2:34",
                   "It’s the same topic on both textbooks"
                   "\n(EXACTLY))  Oussalem 2:35",
                   "What is it that you is playing with"
                   "\n(It is the magnets)"
                   "\nWhat is the magnets?"
                   "\n(It’s like you put them together, and they just attach)"
                   "\nIs this a space shuttle?"
                   "\n(Why are fidgeting with my magnets)"
                   "\nIs this from space?"
                   "\n(No, it isn’t)"
                   "\nVery fascinating  -Mr.Oussalem 2:36",
                   "**I yo math teacher?  Oussalem 2:37**"]

    await ctx.send(f'{random.choice(responses)}')

@client.command(brief='?clap [word]')
async def clap(ctx, *, question):
    await ctx.send(f' *clap clap* {question}?')

@client.command(brief='you know who it is')
async def diego(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/746411118972633112/747620047354331166/jedrik.jpg')
    await asyncio.sleep(.5)
    await ctx.send('https://cdn.discordapp.com/attachments/746411118972633112/747620080770220092/jedrik2.jpg')

@client.command(brief='mabuti poggers')
async def mpog(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/746411118972633112/747627698267881682/drink.png')
    await asyncio.sleep(.5)
    await ctx.send('https://cdn.discordapp.com/attachments/746411118972633112/747627718681559050/pog.png')
    
client.run('NzMyNjI5MDU2NzM0MTAxNTQ2.XxCbTQ.K79s5GkiO7dARKGgpHQv0s__7zM')
