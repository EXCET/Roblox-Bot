import discord
import requests
import colorama
import json
from discord.ext import commands
import random
import string
import threading


file = open('tokens.txt','r')

tokens =  []

use_proxy = "false"

dont_change = "false"

for l in file.readlines():
    tokens.append(l)

r2 = random.choice(tokens)

bot = commands.Bot(command_prefix=["!"], help_command=None)

default_amount = 10

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title='Cooldown',description=f'Wait {round(error.retry_after)} seconds to do this command again!')
        await ctx.send(embed=embed)
    else:
        print(error)

token = "OTM0MTkyOTY5MDcyOTM1MDU1.GKRMAn.FRYmZiyamrQhkk-dAOmfzZqV63BuWafvJCeJfA"

@bot.command()
async def help(ctx):
  embed=discord.Embed(title="Roblox Bot", description="Roblox Friends, And More", color=0xff0000)
  embed.add_field(name="ItemScraper", value="!ritemscrape <id>", inline=False)
  embed.add_field(name="CookieChecker", value="!rcookiecheck <cookie>", inline=False)
  embed.add_field(name="NameChecker", value="!rnamecheck <name>", inline=False)
  embed.add_field(name="CookieGen", value="!rcookiegen", inline=False)
  embed.add_field(name="RobloxFriend", value="!rfriend username", inline=False)
  embed.add_field(name="RobloxInfo", value="!ruserinfo username", inline=False)


#roblox cmds
@bot.command()
async def ritemscrape(ctx, id):
  json = requests.get("https://api.roblox.com/Marketplace/ProductInfo?assetId="+id).json()
  print(colorama.Fore.GREEN + "Asset Id: " + str(json["AssetId"]))
  print(colorama.Fore.GREEN + "Creator Username: " + str(json["Creator"]["Name"]))
  AssetId = ['str(json["AssetId"]))']
  Finishedid = "https://www.roblox.com/catalog/" + id
  await ctx.send("Link: " + Finishedid)
  await ctx.send("Creator: " + json["Creator"]["Name"]) 
  await ctx.send("ItemName: " + json["Name"])
  await ctx.send("ItemDescription: " + json["Description"])
  await ctx.send("ItemCreationDate: " + json["Created"])
  await ctx.send("RobuxAmount: " + str(json["PriceInRobux"]))

@bot.command()
async def rcookiecheck(ctx, cookie):
  r = requests.get("https://api.roblox.com/currency/balance", cookies={".ROBLOSECURITY": str(cookie)})
  if "200" in str(r):
    await ctx.send("Valid Cookie")
  if "200" not in str(r):
    await ctx.send("Invalid Cookie")

@bot.command()
async def rnamecheck(ctx, name):
  r = requests.get(f"https://api.roblox.com/users/get-by-username?username={name}").text
  r = str(r)
  if "User not found" in r:
    await ctx.send("Name Not Used")
  else:
    await ctx.send("Name Used")

@bot.command()
async def rcookiegen(ctx):
  intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
  letters = 'ABCDEF'
  cookies =  intro +  ''.join(random.choices(letters + string.digits, k=732))
  await ctx.send(cookies)

with open('cookies.txt', 'r') as cookies:
    cookies1 = cookies.read().splitlines()

@bot.command()
async def rfriend(ctx, username):
  json = requests.get(f"https://api.roblox.com/users/get-by-username?username="+username).json()
  userId = json["Id"]
  cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_5270895EAF6DBB7741B4B8883DC2C4C012382A0A4F9688CBCB94F9BD8140217FD685FFD2414850AE31FDD9ACDD77DA7935C093CC1D43A1AC5624262A84E052567F005B56D1C3A2111B5293241B274D07080A4C5CAF22E37D2FE124F4A9671D2710762014FB80E1E2A321DD7278AF4A388A205A837205BFBE0FF1DA036E81B3FC8A21D55AA574965427E21D66C5493413BE04955287E622A9E83BACC52F45D0FF542E1709E1C8C610191F7F78C6BC54477C93076A353716BDCE513E7F03710CA369D57EC9995F94B183FFC4A21B95D8A5A108233093AB9E2A4D30316AA1A3E331768265497C79A6A3EDBDD931B41D75995BC4B51B1B99850463A60ACEBB4DE7BD74EE945B09F19DBE23A795240CF8CA5F540AA62FD223796E37CE7595B43F1047AEFAD4B7F999158DECFB495D32EB37749D772A21789AED963C5EDE75FC7B5C9B33247419D58C63E3CEFC5673BC7FD9B0A0B2AA61612396DD99D2D9066E5A9F8EBE708C4F62C83D1A7F41D2924B02345BD447CB4F6AE78BCF275F058CA452294568F927E9"
  session = requests.session()
  session.cookies['.ROBLOSECURITY'] = cookie
  session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
  session.post(f'https://friends.roblox.com/v1/users/{userId}/request-friendship')
  await ctx.send("Sending One Friend To" + username)

@bot.command()
async def ruserinfo(ctx, username):
  json = requests.get(f"https://api.roblox.com/users/get-by-username?username="+username).json()
  userId = json["Id"]
  await ctx.send("Username: ")
  await ctx.send(username)
  await ctx.send("UserId: ")
  await ctx.send(userId)


#spotify cmds
@bot.command()
async def spotifysearch(ctx, search):
  headers = {
        "authorization": f"Bearer {r2}"
    }
  r = requests.put(f'https://api.spotify.com/v1/search/'+search,headers=headers)
  await ctx.send("Song: hi\nArtist: ")

@bot.command()
async def spotifyfollow(ctx, id):
    embed = discord.Embed(title='Spotify Followers', description=f'Sending Followers to {id}')
    await ctx.send(embed=embed)
    headers = {
        "authorization": f"Bearer {r2}"
    }
    r = requests.put(f'https://api.spotify.com/v1/me/following?type=artist&ids={id}',headers=headers)
          
@bot.command()
async def spotifylike(ctx, id):
    embed = discord.Embed(title='Spotify Likes', description=f'Sending Likes to {id}')
    await ctx.send(embed=embed)

    headers = {
        "authorization": f"Bearer {random.choice(tokens)}"
    }
    r = requests.put(f'https://api.spotify.com/v1/me/tracks?ids={id}',headers=headers)

#twitch cmds

def get_user(channel_name):

    json = {"operationName": "ChannelShell",
            "variables": {
                "login": channel_name
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe"
                }
            }
        }

    headers = {
        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }
    r = requests.post('https://gql.twitch.tv/gql', json=json, headers=headers)
    return r.json()['data']['userOrError']['id']

color = 0xfb00ff

bot_channel1 = 1005106139798720562

dont_change = False

@bot.command()
async def tfollow(ctx, channel_name):
    if ctx.channel.id == int(bot_channel1):
        if dont_change == True:
            print("Change config dont_change to false")
        else:
            username = get_user(channel_name)

            follow_amount = default_amount

            embed = discord.Embed(title="Twitch followers", description=f"Sending **{follow_amount}** Twitch Followers to **{channel_name}**", color=color)
            await ctx.send(embed=embed)


            def follow_user():
                
                token = open('tokens.txt', 'r').read().splitlines()
                tokens = random.choice(token)

                proxy_list = open('proxies.txt','r').read().splitlines()


                proxy = random.choice(proxy_list)
                proxies = {
                'http': f'http://{proxy}',
                'https':f'http://{proxy}'
                }

                headers = {
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-GB",
                    "Authorization": f"OAuth {tokens}",
                    "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
                    "Connection": "keep-alive",
                    "Content-Length": "541",
                    "Content-Type": "text/plain;charset=UTF-8",
                    "Host": "gql.twitch.tv",
                    "Origin": "https://www.twitch.tv",
                    "Referer": "https://www.twitch.tv/",
                    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-site",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                    }

                json = {
                "operationName": "FollowButton_FollowUser",
                "variables": {
                    "input": {
                    "disableNotifications": False,
                    "targetID": f"{username}"
                    }
                },
                "extensions": {
                    "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "800e7346bdf7e5278a3c1d3f21b2b56e2639928f86815677a7126b093b2fdd08"
                    }
                }
                }
                if use_proxy == False:
                    r = requests.post('https://gql.twitch.tv/gql', headers=headers, json=json)
                else:
                  r = requests.post('https://gql.twitch.tv/gql', headers=headers, json=json, proxies=proxies)

                  threading.Thread(target=follow_user).start()

@bot.command()
async def tusernamecheck(ctx, user):
   r = requests.get(f'https://www.twitch.tv/{user}')
   if r.status_code == 200:
        await ctx.send("Twitch Name Taken")
   else:
        await ctx.send("Twitch Name Valid")

def namegen():

     length = random.randint(30, 31)
     eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
     "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"

     return ''.join(random.choice(eval) for i in range(length))

@bot.command()
async def ttokengen(ctx):
  
     tokens = namegen()
     await ctx.send(tokens)

#instagram cmds

#other cmds

@bot.command()
async def bronze(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> ,bronze')
    auth = ctx.author
    member = ctx.guild.get_member(ctx.author.id)
    await ctx.send("Make sure `discord.gg/AzGjF9EW` is in your bio to claim!")
    
    for status in member.activities:
        if isinstance(status, discord.CustomActivity):
            if status.name != 'discord.gg/AzGjF9EW':
                    await ctx.message.delete()
                    embed = discord.Embed(color=0xe91e63, description="You need to set your status to 'discord.gg/AzGjF9EW'")
                    await ctx.send(embed=embed)
            else:
                if status.name == 'discord.gg/AzGjF9EW':
                    role = discord.utils.get(ctx.guild.roles, name="Bronze")
                    user = ctx.message.author
                    await user.add_roles(role)
                    embed = discord.Embed(color=0xe91e63, description=f"I have given you Bronze Role! {member.mention}")
                    await ctx.send(embed=embed)

            

#tiktok cmds

@bot.command()
async def ttusercheck(ctx, user):
  r = requests.get(f'https://www.tiktok.com/@{user}')
  if r.status_code == 200:
        await ctx.send("Tiktok Name Taken")
  else:
        await ctx.send("Tiktok Name Not Taken")

@bot.command()
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=1001631084011855952&permissions=0&scope=bot")

@commands.is_owner()
@bot.command()
async def getguild(ctx):
    for i in bot.guilds:
      try:
        i2 = random.choice(i.text_channels)
        b = await i2.create_invite()
        await ctx.send(b)
      except Exception as e:
        print(e)



bot.run(token)
