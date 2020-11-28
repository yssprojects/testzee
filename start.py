from telethon import TelegramClient, events, Button
import requests
from headers import headers
import urls
import os
#import asyncio
from youtube_dl import YoutubeDL
#from flask import request


client = TelegramClient('anfghohn', int(os.environ.get("APP_ID" )), os.environ.get("API_HASH")).start(bot_token= os.environ.get("TG_BOT_TOKEN"))
@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    chat = await event.get_chat()
    await client.send_message(chat,"""Hi Im Asuran """)
    

@client.on(events.NewMessage(pattern='(?i)https://www.zee5.com'))
async def handler(event):
    link =event.text.split('/')[-1] 
    chat = await event.get_chat()
    w =link
    markup = client.build_reply_markup(Button.url("https://www.zee5.com/tvshows/details/sembaruthi/0-6-675/sembaruthi-november-18-2020/0-1-manual_7adlhget67b0"+link))
    req1 = requests.get(urls.token_url1, headers=headers).json()
    req2 = requests.get(urls.platform_token).json()["token"]
    headers["X-Access-Token"] = req2
    req3 = requests.get(urls.token_url2, headers=headers).json()           
    r1 = requests.get(urls.search_api_endpoint + w,headers=headers, params={"translation":"en", "country":"IN"}).json()
    g1 = (r1["hls"][0].replace("drm", "hls") + req1["video_token"])
   # await client.send_file(chat,r1["image_url"],caption = r1["title"])
    markup = client.build_reply_markup(Button.url("Zee5 Stream",urls.stream_baseurl+g1))
    await client.send_message(chat, "Support @SerialCoIn & @urlicupload\n\n"+"🎥 "+r1["title"]+"\n\n📑 "+r1["description"],file=r1["image_url"], buttons=markup)   

    #s = requests.Session()
   #aq1 = s.get(g1 + req3["video_token"], headers=headers)
   #c1 = re.findall("index.*", aq1.text)
   #markup = client.build_reply_markup(Button.url("Stream",urls.stream_baseurl+g1),
   #Button.url("Zee5 Stream 144p",urls.stream_baseurl+c1[1]),
   #Button.url("Zee5 Stream 240p",urls.stream_baseurl+c1[2]),
   #Button.url("Zee5 Stream 360p",urls.stream_baseurl+c1[3]))
    
    
            #rgx = w
   # await client.send_message(chat, g1)
   #await client.send_message(chat,"445")
    
@client.on(events.NewMessage(pattern='(?i)https://www.mxplayer.in'))
async def handler(event):
    link =event.text.split('/')[-1]
    video_d = "https://llvod.mxplay.com/"
    A =requests.get("https://api.mxplay.com/v1/web/detail/video?type=movie&id="+link+"&platform=com.mxplay.desktop&device-density=2&userid=30bb09af-733a-413b-b8b7-b10348ec2b3d&platform=com.mxplay.mobile&content-languages=hi,en,ta").json()
    chat = await event.get_chat()
    markup = client.build_reply_markup(Button.url("Mx Stream",video_d+A["stream"]['hls']['high']))
    await client.send_message(chat," support @urlicupload   "+A["title"],buttons=markup)
    print(A)
    print(link)
@client.on(events.NewMessage(pattern='(?i)https://www.hotstar.com/in/'))
async def handler(event):
    link =event.text
    print(link)
    #import youtube_dl
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    with ydl:
        result = ydl.extract_info(
        link,
        download=True # We just want to extract the info
    )
    await client.send_message(chat,result)
    
@client.on(events.NewMessage(pattern='(?i)/ls'))
async def handler(event):
    link =event.text.split(" ")[1]
    e = os.listdir(link)
    chat = await event.get_chat()
    c = "|"
    #str1.join(s)
    #print(c)
    await client.send_message(chat,c.join(e))
@client.on(events.NewMessage(pattern='(?i)sm'))
async def handler(event):
    link =event.text.split(" ")[1]
    print(link)
    chat = await event.get_chat()
    await client.send_file(chat, '/Download'+link,force_document=True)
    
    
    
    
client.start()
client.run_until_disconnected()
