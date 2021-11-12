# インストールした discord.py を読み込む
import discord 
from discord.ext import commands 
import valorant
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'THi5IsDuMMyaCCesSTOK3n00.Cl2FMQ.ThIsi5DUMMyAcc3s5ToKen0000'
# 接続に必要なオブジェクトを生成
client = discord.Client()
CHANNEL_ID = 573211321638846499


@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('私が来た')

# メッセージ受信時に動作する処理

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        print(";nekoが実行されました")
        await message.channel.send('にゃーん')
    
    if message.content == ';mapAgent':
        print("mapAgentを開始しました")
        await message.channel.send(await valorant.mapAgent())
    
    if message.content == ';namAgent':
        print("namAgentを開始しました")
        await message.channel.send(await valorant.namAgent())
    
    if message.content == ';help':
        print("helpを開始しました")
        await message.channel.send(await valorant.help_com())


"""
@bot.command()
async def namA(ctx):
    print("namAgentを開始しました")
    await ctx.send(valorant.namAgent())
"""

"""
        await message.channel.send("DUELSITの数を入力！")
        wait_message = await client.wait_for(message.content)
        print("受け取った")
        role_nam.append(int(wait_message))

        await message.channel.send("sentinelの数を入力！")
        wait_message = await client.wait_for(int("message"))
        role_nam.append(int(wait_message))
        await message.channel.send(name + "の数は" + wai_message + "だよ！")

        await message.channel.send("smokeの数を入力！")
        wait_message = await client.wait_for(int("message"))
        role_nam.append(int(wait_message))
        await message.channel.send(name + "の数は" + wai_message + "だよ！")

        await message.channel.send("いにしの数を入力！")
        wait_message = await client.wait_for(int("message"))
        role_nam.append(int(wait_message))
        await message.channel.send(name + "の数は" + wai_message + "だよ！")
    
        if sum(role_nam) == 5:
            result.append(random.sample(DUELIST,role_nam[0]))
            result.append(random.sample(SENTINEL,role_nam[1]))
            result.append(random.sample(SMOKE,role_nam[2]))
            result.append(random.sample(INISI,role_nam[3]))
            await message.channel.send(result)

        else :
            channel.send("入力オーバーです。最初からやり直してね")
"""

# Botの起動とDiscordサーバーへの接続
client.run('ODk1NTA5MTM2OTU4MTY1MDEz.YV5l4A.OSghO_PytmoJv7pqVtx_XjqKi4A')