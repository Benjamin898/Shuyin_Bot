from ast import Try
import asyncio
import sys
import os
import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime
from welcome_editor import *
import functools
import typing



TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(intents=discord.Intents.all(), command_prefix= "s!") # Set Prefix


######### Ordenar esto y añadir un mensajito abajo diciendo "espero que disfrutes bla bla..." #########

@bot.event
async def on_member_join(member, avatar_png: discord.Member = None):
    
    channel = bot.get_channel(1030300264231608322) # change to your channel id
    member1 = "<@318797989449695233>"
    member2 = "<@686090046603788352>"
    embed = discord.Embed(title=f"¡¡Bienvenido a {member.guild.name}!!", description=f"- Espero que te diviertas **{member.name}** y que pases un buen rato! Si tienes alguna duda no dudes en consultar a {member1} o {member2}.", color=0x9680b6)
    
    
    
    avatar = member.avatar

    # save a asset to a file
    try:
        with open('./Avatar/avatar.png', 'wb') as f:
            await avatar.save(f)
    except:
        avatar = member.default_avatar
        
        with open('./Avatar/avatar.png', 'wb') as f:
            await avatar.save(f)


    img_editor_text(str(member.name)+"#"+str(member.discriminator))
    
    file = discord.File("./Img/welcome_edit.png", filename="welcome_edit.png")
    embed.set_image(url="attachment://welcome_edit.png")

    embed.timestamp = datetime.now()
    await channel.send(file=file, embed=embed)

    #print(f'{member.name} joined the server')

############################################


"""
@bot.command(name='chiste') ### Testing
async def function_joke(ctx):
    chiste = pyjokes.get_joke("es", "neutral")
    await ctx.send(chiste)
"""
@bot.command(name='part1') ### Testing
async def message_colours(ctx):
    
    channel = bot.get_channel(1029854171316355162) # change to your channel id
    embed = discord.Embed(title=None, 
    description=f":sparkles: Este servidor de Discord busca reunir a una comunidad que quiera compartir sus gustos, divertirse, crecer y apoyar a los demás."+"\n"+"\n"+
    "**__Reglas para ser un buen Oshi ´ ▽ ` )ﾉ __**"+"\n"+"\n"+
    "✧ Ser amable y respetuoso."+ "\n" +
    "✧ Usar un nick reconocible de Twitch."+ "\n" +
    "✧ No se acepta ningún tipo de discriminación."+ "\n" +
    "✧ Usar los canales respectivos para cada temática evitando el spam."+ "\n"+
    "✧ No profanar a la Lunita de ninguna manera >:["+ "\n"+"\n"+
    " (─‿‿─)･ﾟ✧ ", 
    color=0xA020F0)
    embed.set_image(url="https://i.imgur.com/YCVeRXf.png")
    await channel.send(embed=embed)

"""
@bot.command(name='part2') ### Testing
async def message_colours(ctx):
    
    url = "https://tenor.com/view/surgb-_radcollab-strandedunicorns-nft-strandedunicorns-rgb-gif-25040584"
    channel = bot.get_channel(1030731608271097927) # change to your channel id
    embed = discord.Embed(title=None, 
    description=f"<:choco:1043310572462161970>  **__Selecciona una red:__** *Aquí podrás elegir una o varias redes sociales en las que se encuentra Shuyin-sama, al elegir alguna, recibirás notificaciones de dicha(s) red(es) dentro del servidor. Las redes disponibles son las siguientes:*"+"\n"+"\n"+
    "<:twitch:1043313538019631244>  ✦ <@&1030299584913752094> 　 <:youtube:1043313549864349696>  ✦ <@&1030299130674806895>"+ "\n" +
    "<:tiktok:1043313525772259378>   ✦ <@&1030299701649608744> " +"\n"+"\n" +
    " <:hand_cursor:1043049505370669077> - Para seleccionar una red, simplemente reacciona con el emoji correspondiente, este hará efecto inmediatamente.", 
    color=0xA020F0)
    
    await channel.send(embed=embed)
"""

"""
@bot.command(name='part3') ### Testing
async def message_colours(ctx):
    
    channel = bot.get_channel(1030731608271097927) # change to your channel id
    embed = discord.Embed(title=None, 
    description=f"<:pdsf:1045035788250914956>  **__Selecciona un videojuego:__** *En este apartado podrás seleccionar uno o varios videojuegos que sean de tu agrado, pudiendo recibir notificaciones de otros usuarios que estén interesados en jugar con personas con los mismos gustos o simplemente notificar información respecto al mismo. Los roles de videojuegos disponibles son las siguientes:*"+"\n"+"\n"+
    "<:ff14:1045028776343506965>  ✦ <@&1045027813092245504> 　 <:dbd:1045029553703227483>  ✦ <@&1045027798236012554>"+ "\n" +
    "<:ow2:1045028818571772004> ✦ <@&1045027858420072498> 　　　<:lol:1045028892290859090> ✦ <@&1045027765595947069>" +"\n"+
    "<:valorant:1045028853636145242>  ✦ <@&1045027714920361994>"+"\n\n"
    " <:hand_cursor:1043049505370669077> - Para seleccionar un videojuego, simplemente reacciona con el emoji correspondiente, este hará efecto inmediatamente y podrás recibir notificaciones tanto de usuarios como del servidor en algunos casos.", 
    color=0xA020F0)
    
    await channel.send(embed=embed)
"""
################ RGB SEND ################

@bot.command(name='rgb') ### Testing
async def message_colours(ctx):
    
    url = "https://tenor.com/view/surgb-_radcollab-strandedunicorns-nft-strandedunicorns-rgb-gif-25040584"

    channel = bot.get_channel(1030731608271097927) # change to your channel id
    
    await channel.send(url)

@bot.command(name='banner') ### Testing
async def message_colours(ctx):
    
    url = "https://i.imgur.com/YCVeRXf.png"

    channel = bot.get_channel(1030731608271097927) # change to your channel id
    
    await channel.send(url)


######### events ##########

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Streaming(name="🍣 Catando oshis -.-", url='https://www.twitch.tv/yashiwright'))


##############################
@bot.command()
#Create a multiple poll function with timer and progressive bars
async def poll(ctx, *args):
    #Check if there is a question
    if len(args) == 0:
        await ctx.send("Please enter a question")
        return
    #Check if there are more than 10 options
    if len(args) > 10:
        await ctx.send("Please enter less than 10 options")
        return
    #Check if there is a timer
    print(args[0][-1])  
    if args[0].isdigit():
        timer = int(args[0])
        args = args[1:]
        
    else:
        timer = 60
    #Create the embed
    embed = discord.Embed(title=f"🆔 Votación creada por: {ctx.author} \n#######\n📕 Pregunta: {args[0]}\n--------\n> 🧾 Opciones:", color=0x000000)
    today = datetime.today()
    embed.set_footer(text=f"\n🕒 La votación se cerrará en: {today}")
    #Add the options
    reactions=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    for i in range(1, len(args)):
        embed.add_field(name=f"{reactions[i-1]} - {args[i]}", value="0%", inline=False)
    #Send the embed
    message = await ctx.send(embed=embed)
    #Add the reactions
    for i in range(1, len(args)):
        await message.add_reaction(f"{i}\N{COMBINING ENCLOSING KEYCAP}")
    #Check if there is a timer
    if timer > 0:
        #Wait for the timer
        await asyncio.sleep(timer)
        #Get the message
        message = await ctx.fetch_message(message.id)
        #Get the reactions
        reactions = message.reactions
        #Create the embed
        embed = discord.Embed(title=f"🎪 Resultados de la votación\n--------\n📕 Pregunta: {args[0]}\n--------\n> 🧾 Opciones:", color=0x000000)
        #Add the options
        for i in range(1, len(args)):
            embed.add_field(name=f"{reactions[i-1]} - {args[i]}", value=f"{round(reactions[i-1].count/len(reactions)*100)}%", inline=False)
        #Edit the embed
        await message.edit(embed=embed)

##############################

@bot.command(name= "reiniciar")
async def restart(ctx):
    mod_role = discord.utils.get(ctx.guild.roles, id=1041774005553737769)
    adm_role = discord.utils.get(ctx.guild.roles, id=1029962959096643636)
    if mod_role in ctx.author.roles or adm_role in ctx.author.roles:
        await ctx.send("Me estoy reiniciando, bip...")
        restart_bot()
    else:
        await ctx.send("No tienes permisos para ejecutar este comando, pequeño Oshi ^^<.")

#############################

if __name__ == '__main__':
    bot.run(TOKEN)

    

