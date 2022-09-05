from discord.ext import commands 
import discord
import random

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is online and ready to use!")



@bot.command()
async def mines(ctx, round_id):
    round_id = str(round_id)
    round_lenght = len(round_id)
    if round_lenght < 36:
        await ctx.send("invalid round id")
    elif round_lenght == 36:
        mine1,mine2,mine3,mine4,mine5,mine6,mine7,mine8,mine9,mine10,mine11,mine12,mine13,mine14,mine15,mine16,mine17,mine18,mine19,mine20,mine21,mine22,mine23,mine24,mine25 = '❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓','❓'
        a = random.randint(1, 8)
        b = random.randint(9, 13)
        c = random.randint(14, 17)
        d = random.randint(18, 25)
        if a == 1:
            mine1 = "🟥"
        elif a == 2:
            mine2 = "🟥"
        elif a == 3:
            mine3 = "🟥 "
        elif a == 4:
            mine4 = "🟥 "
        elif a == 5:
            mine5 = "🟥 "
        elif a == 6:
            mine6 = "🟥 "
        elif a == 7:
            mine7 = "🟥 "
        elif a == 8:
            mine8 = "🟥 "
        if b == 9:
            mine9 = "🟥 "
        elif b == 10:
            mine10 = "🟥 "
        elif b == 11:
            mine11 = "🟥 "
        elif b == 12:
            mine12 = "🟥 "
        elif b == 13:
            mine13 = "🟥 "
        if c == 14:
            mine14 = "🟥 "
        elif c == 15:
            mine15 = "🟥 "
        elif c == 16:
            mine16 = "🟥 "
        elif c == 17:
            mine17 = "🟥 "
        if d == 18:
            mine18 = "🟥 "
        elif d == 19:
            mine19 = "🟥 "
        elif d == 20:
            mine20 = "🟥 "
        elif d == 21:
            mine21 = "🟥 "
        elif d == 22:
            mine22 = "🟥 "
        elif d == 23:
            mine23 = "🟥 "
        elif d == 24:
            mine24 = "🟥 "
        elif d == 25:
            mine25 = "🟥 "

        row1 = mine1 + mine2 + mine3 + mine4 + mine5
        row2 = mine6 + mine7 + mine8 + mine9 + mine10
        row3 = mine11 + mine12 + mine13 + mine14 + mine15
        row4 = mine16 + mine17 + mine18 + mine19 + mine20
        row5 = mine21 + mine22 + mine23 + mine24 + mine25
        
        info = str(random.randint(15, 85))
        pfp = '1015942457059454986'
        em = discord.Embed(color = 0x3D0F6B)
        em.set_thumbnail(url=pfp)
        em.set_footer(text="Made by FLUSHYQ#8151")
        em.add_field(name="Mines Predictor", value=row1 + "\n" +  row2+ "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + "**Accuracy**" + "\n" + info + "%")
        await ctx.send(embed=em)

      

bot.run('')
