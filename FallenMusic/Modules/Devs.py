import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
@app.on_message(
    command(["صورص","سورس","السورس","هورس", "حصان"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/46d833b85e364e3bc20ac.jpg",
        caption=f"""
╭──── • ◈ • ────╮ 
么  [𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒓𝒂𝒆♡](t.me/T7_AU)
么[𝗧𝗘𝗧𝗢](t.me/G_7_Rr)
╰──── • ◈ • ────╯ 
  
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗧𝗘𝗧𝗢", url=f"https://t.me/G_7_Rr"), 
                ],[
                    InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝙀 𝙏𝙀𝙏𝙊", url=f"t.me/T7_AU"),
                ],

            ]

        ),

    )
@app.on_message(
   command(["تيتو"])
)

@app.on_edited_message(command(["تيتو"])
)
async def Teto(client: Client, message: Message):
  usr = await app.get_users(6133404544)
  user = await client.get_chat(6133404544)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(6133404544,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 6133404544 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(6133404544, f"مبرمجي العزيز {Tetous}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
@app.on_message(
    command(["تيتو","المبرمج مودي","تيتو"])
)
@app.on_edited_message(command(["احمد","المبرمج احمد","احمد"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(6133404544)
  user = await client.get_chat(6133404544)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(6133404544,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 6133404544 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(6133404544, f"مبرمجي العزيز {Tetous}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
@app.on_message(
    command(["مواململتو","المبلملمرمج املم","المطور مولتو"])
)
@app.on_edited_message(command(["ااااااااااااب"])
)
async def zohary(client: Client, message: Message):
  usr = await app.get_users(2143824894)
  user = await client.get_chat(2143824894)
  Bio = user.bio
  name = usr.first_name
  async for photo in app.get_chat_photos(2143824894,limit=1):
    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - {usr.mention} 🕷
                       
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @{usr.username} 🕷
                       
ႦᎥ᥆ | - {Bio} 🕷       
                         
Ꭵժ | - 6133404544 🕷 """,
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )
    zoharyus = usr.mention
    sender_id = message.from_user.id
    message_link = await Telegram.get_linok(message)
    sender_name = message.from_user.first_name
    invitelink = await app.export_chat_invite_link(message.chat.id)
    await app.send_message(6133404544, f"مبرمجي العزيز {لفمقمق}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                        
