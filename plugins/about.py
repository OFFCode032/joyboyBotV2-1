import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6769975697:AAEKNVPAfieMX2IiKbDIpBJxX-gr4-o1_Dk')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"<b>▫️ Name:-𝟺ɢʙ Rᴇɴᴀᴍᴇʀ Bᴏᴛ\n◽️ Creater :-[𓊈Sᴏɴᴀʟɪ Sᴀʜᴀ𓊉](https://t.me/sonali_sahaibot)\n▫️ Language :-Python3\n▫️ Library :- Pyrogram 2.0\n▫️ Server :- Unknown\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))}</b>", quote=True)
