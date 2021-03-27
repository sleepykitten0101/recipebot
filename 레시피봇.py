import asyncio
import discord
import os

client = discord.Client()

# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("Your bot :") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("Is ready!")
    print("----------------")

    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("MEOW. 서버 레시피봇 입니다!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("`레시피 도움을 입력해보세요!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content == '`레시피 텍스트':
        channel = message.channel
        await channel.send('1.2.3 실행')

    elif message.content == "`레시피":
        embed = discord.Embed(title="레시피봇 오류 ⚠", description='''
        **``레시피 [레시피명]` 으로 레시피를 검색해주세요!**
        레시피 목록을 보고 싶으시다면 **``레시피 목록`**을 입력해주세요!
          ''', color=0xFF0000)
        embed.set_footer(text="send by. 𝔓𝔲𝔯𝔢 𝔙𝔞𝔫𝔦𝔩𝔩𝔞 ℭ𝔬𝔬𝔨𝔦𝔢#9374")
        await message.channel.send(embed=embed)

    elif message.content == '`레시피 목록':
        embed=discord.Embed(title="레시피 목록이 궁금하시다면 아래 링크에 들어가주세요!", description="https://blog.naver.com/sleepykitten0101/222273661248", color=0xCCEEFF)
        embed.set_author(name="레시피 목록 🍨", url="https://www.flaticon.com/svg/vstatic/svg/3198/3198831.svg?token=exp=1615881427~hmac=9d16269cb0f9aede31bc9bbfb206b4bd")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/819929705901588500/41b06a8c4d51ee6d782ad13cc0c6aaa6.png?size=4096")
        embed.set_footer(text="send by. 𝔓𝔲𝔯𝔢 𝔙𝔞𝔫𝔦𝔩𝔩𝔞 ℭ𝔬𝔬𝔨𝔦𝔢#9374")
        await message.channel.send(embed=embed)
    
    elif message.content == "`레시피 실":
        embed = discord.Embed(title="실 제작방법 🧶", description='''
          1. '슷칼봇 무역' 명령어로 '장난감 요요' 제작
          2. '[아이템] 실 절단용 검 🗡'으로 요요 실 획득!
          ''', color=0x01C00E)
        embed.set_footer(text="일반 아이템")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 막대":
        embed = discord.Embed(title="막대 제작방법 📏", description='''
          1. 크시로 '나무' 라고 입력했을 때 '막대 획득!' 이라고 말하게 하기
          ''', color=0x01C00E)
        embed.set_footer(text="일반 아이템")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 실 절단용 검":
        embed = discord.Embed(title="실 절단용 검 제작방법 🗡", description='''
          1. 'UpSword' 로 검 레벨 10 이상 만들고 판매하기
          ''', color=0x01C00E)
        embed.set_footer(text="일반 아이템")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 실 낚싯대":
        embed = discord.Embed(title="실 낚싯대 제작방법 🦯", description='''
          1. '[아이템] 실' 과 '[아이템] 막대'를 가지고 있는 상태에서 확인의 텐트에 실 낚싯대를 달라고 하기
          ''', color=0xFDF458)
        embed.set_footer(text="레벨업 아이템")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 캣닙":
        embed = discord.Embed(title="캣닙 제작방법 🌿", description='''
          1. '슷칼봇 텃밭' 명령어로 식물 1회 재배하기
          ''', color=0x01C00E)
        embed.set_footer(text="일반 아이템")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 천":
        embed = discord.Embed(title="천 제작방법 🧦", description='''
          1. 비밀 커맨드입니다. !을 사용하면 될지도...?
          ''', color=0xC767FE)
        embed.set_footer(text="에픽 아이템")
        await message.channel.send(embed=embed)
    
    elif message.content == "`레시피 깃털":
        embed = discord.Embed(title="깃털 제작방법 🦢", description='''
          1. 출석체크 15회 시 지급
          ''', color=0x33B0FF)
        embed.set_footer(text="레어 아이템")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 깃털 낚싯대":
        embed = discord.Embed(title="깃털 낚싯대 제작방법 🦯", description='''
          1. '[아이템] 깃털' 과 '[아이템] 막대'를 가지고 있는 상태에서 확인의 텐트에 깃털 낚싯대를 달라고 하기
          ''', color=0x33B0FF)
        embed.set_footer(text="레어 아이템")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 천 낚싯대":
        embed = discord.Embed(title="천 낚싯대 제작방법 🦯", description='''
          1. '[아이템] 천' 과 '[아이템] 막대'를 가지고 있는 상태에서 확인의 텐트에 천 낚싯대를 달라고 하기
          ''', color=0x33B0FF)
        embed.set_footer(text="레어 아이템")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 도움":
        embed = discord.Embed(title="레시피 도움 🍨", description='''
          https://blog.naver.com/sleepykitten0101/222273661248
          ''', color=0xCCEEFF)
        embed.set_footer(text="send by. 𝔓𝔲𝔯𝔢 𝔙𝔞𝔫𝔦𝔩𝔩𝔞 ℭ𝔬𝔬𝔨𝔦𝔢#9374")
        await message.channel.send(embed=embed)

    elif message.content == "`레시피 초대":
        embed = discord.Embed(title="레시피 초대 🍨", description='''
          **초대 링크는 이거예요!**
          https://discord.com/api/oauth2/authorize?client_id=819929705901588500&permissions=0&scope=bot
          ''', color=0xCCEEFF)
        embed.set_footer(text="send by. 𝔓𝔲𝔯𝔢 𝔙𝔞𝔫𝔦𝔩𝔩𝔞 ℭ𝔬𝔬𝔨𝔦𝔢#9374")
        await message.channel.send(embed=embed)     
 
    elif message.content.startswith('`레시피'):
        embed = discord.Embed(title="레시피봇 오류 ⚠", description='''
          **음..❓ 아무리 명령어를 뒤져봐도 그런 레시피는 없네요💦**
          ''', color=0xFF0000)
        embed.set_footer(text="send by. 𝔓𝔲𝔯𝔢 𝔙𝔞𝔫𝔦𝔩𝔩𝔞 ℭ𝔬𝔬𝔨𝔦𝔢#9374")
        await message.channel.send(embed=embed)

    
access_token = os.environ["BOT_TOKEN]
client.run(access_token)
