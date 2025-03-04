import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import wget

import core as helper
from utils import progress_bar
from vars import api_id, api_hash, bot_token
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)


@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
       f"**𝗗𝗲𝗮𝗿 𝗠𝗲𝗺𝗯𝗲𝗿𝘀,**\n\n**𝘔𝘺𝘴𝘦𝘭𝘧 𝘢 𝘛𝘟𝘛 𝘋𝘖𝘞𝘕𝘓𝘖𝘈𝘋𝘌𝘙 𝘉𝘖𝘛.**\n**To Extract .txt File /ajpython.**\n**To Stop /stop**\n\n𝐌𝐀𝐃𝐄 𝐁𝐘: ᏰᎻᏬᎷᎨᎻᎯᏒ", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝕺𝖋𝖋𝖎𝖈𝖎𝖆𝖑 𝕮𝖍𝖆𝖓𝖓𝖊𝖑 " ,url=f"https://t.me/BHUMIHARxTXT") ],
                    [
                    InlineKeyboardButton("𝔒𝔴𝔫𝔢𝔯: ᗷᕼᑌᗰIᕼᗩᖇ" ,url="https://t.me/Thebhumihar") ]
            ]))

@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Ruk gya Bhumihar ji ☺**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["bhumihar"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('**۞ 𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐓𝐗𝐓 𝐅𝐈𝐋𝐄 \n𝐌𝐀𝐃𝐄 𝐁𝐘: ᏰᎻᏬᎷᎨᎻᎯᏒ**')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(x)
        await input.delete(True)    
        file_name, ext = os.path.splitext(os.path.basename(x))


        path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**𝐫𝐮𝐤 𝐣𝐚 𝐛𝐬𝐝𝐤**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**۞ 𝐓𝐨𝐭𝐚𝐥 𝐋𝐢𝐧𝐤𝐬 𝐅𝐨𝐮𝐧𝐝 𝐚𝐫𝐞: ** **{len(links)}**\n\n**𝐒𝐞𝐧𝐝 𝐈𝐧𝐝𝐞𝐱 𝐍𝐮𝐦𝐛𝐞𝐫 𝐅𝐫𝐨𝐦 𝐰𝐡𝐞𝐫𝐞 𝐲𝐨𝐮 𝐬𝐭𝐚𝐫𝐭:** **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**۞ 𝐄𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**╭──────◈𝐐𝐮𝐚𝐥𝐢𝐭𝐲◈──────╮\n | ● 360ᴘ\n | ● 48𝟶ᴘ\n | ● 72𝟶ᴘ\n | ● 10𝟾𝟶ᴘ\n╰────────◈ΛJ◈───────╯**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("**۞ 𝐄𝐧𝐭𝐞𝐫 𝐘𝐨𝐮𝐫  𝐍𝐚𝐦𝐞 𝐨𝐫 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞:**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ＭＡＲＣＯ™⁪⁬⁮⁮⁮"
    if raw_text3 == 'ＭＡＲＣＯ™':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("𝐒𝐞𝐧𝐝 𝐌𝐞 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐔𝐑𝐋:**\nEg : https://envs.sh/az_.jpg")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = raw_text6
    if thumb.startswith("http://") or thumb.startswith("https://"):
        try:
            wget.download(thumb, out="thumb.jpg")
            thumb = "thumb.jpg"
        except Exception as e:
            thumb = "no"
            print(f"Error Downloading Thumbnail: {e}")
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:    
                async with ClientSession() as session:    
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                                         'Accept-Language': 'en-US,en;q=0.9', 
                                                         'Cache-Control': 'no-cache', 
                                                         'Connection': 'keep-alive', 
                                                         'Pragma': 'no-cache', 
                                                         'Referer': 'http://www.visionias.in/', 
                                                         'Sec-Fetch-Dest': 'iframe', 
                                                         'Sec-Fetch-Mode': 'navigate', 
                                                         'Sec-Fetch-Site': 'cross-site', 
                                                         'Upgrade-Insecure-Requests': '1', 
                                                         'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                                                         'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 
                                                         'sec-ch-ua-mobile': '?1', 
                                                         'sec-ch-ua-platform': '"Android"',}) as resp:    
                        text = await resp.text()    
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if '/master.mpd' in url and not '/drm/' in url:
                id = url.split("/")[-2]
                pwtoken = os.getenv('pwtoken')
                url = f''
                print(url)

            elif "tencdn.classplusapp" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "media-cdn-a.classplusapp" in url or "media-cdn.classplusapp" in url:
                headers = {'Host': 'api.classplusapp.com', 'x-access-token': '', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
                params = (('url', f'{url}'),)
                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                url = response.json()['url']	

            elif "apps-s3-jw-prod.utkarshapp.com" in url:
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif 'Key-Pair-Id' in url:
                    url = None
               
            elif "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth='
                url = url.split("bcov_auth")[0]+bcov
            
            elif ".pdf" in url:
                url = url.replace(" ","%20")

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)})  𝗔𝗝 𝗣𝗬𝗧𝗛𝗢𝗡~{name1[:60]}'

            if "embed" in url:
                ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"
            elif "youtube" in url:
                ytf = f"bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]/best[height<={raw_text2}][ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url and (url.endswith(".mp4") or "Expires=" in url):
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            #if "jw-prod" in url and (url.endswith(".mp4") or "Expires=" in url):
                #user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"             
                #cmd = f'yt-dlp -o "{name}.mp4" --user-agent "{user_agent}" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
        
            try:  
                
                cc = f'[📹] ᐯIᗪ_Iᗪ ⇛ {str(count).zfill(3)}.\n𝐕𝐢𝐝𝐞𝐨 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 ⇛ {name1} {res} 𝕭𝖍𝖚𝖒𝖎𝖍𝖆𝖗.mkv\n\n<pre><code>🔖 Batch Name: {raw_text0}</code></pre>**\n\n📥 𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲: {MR}🗿\n\n'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                cc1 = f'[📁]  ᖴIᒪE_Iᗪ ⇛ {str(count).zfill(3)}.\n𝐅𝐢𝐥𝐞 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 ⇛ {name1} 𝕭𝖍𝖚𝖒𝖎𝖍𝖆𝖗.pdf\n\n<pre><code>🔖 Batch Name: {raw_text0}</code></pre>\n\n📥 𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲: {MR}🗿\n\n'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**BHUMIHAR**\n\n➢ **𝐍𝐚𝐦𝐞 » `{name}\n➢ 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n➢ 𝐕𝐢𝐝𝐞𝐨 𝐔𝐑𝐋 » **𝐍𝐇𝐈 𝐃𝐈𝐊𝐇𝐀𝐔𝐍𝐆𝐀**\n\n 𝐌𝐀𝐃𝐄 𝐁𝐘: ᏰᎻᏬᎷᎨᎻᎯᏒ\n"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**Ξ 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐈𝐍𝐆 𝐄𝐑𝐑𝐎𝐑 Ξ**\n{str(e)}\n➢ **𝐍𝐚𝐦𝐞** » {name}\n➢ **𝐋𝐢𝐧𝐤** » **Malik Smjh Jayenge**"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**۞ BHUMIHAR☺ ۞\n𝐈'𝐌 𝐃𝐎𝐍𝐄.☺**")


bot.run()
