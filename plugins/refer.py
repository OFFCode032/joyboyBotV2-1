from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📲 ᴄʟɪᴄᴋ ᴛᴏ ʀᴇғᴇʀ 📲" ,url=f"https://t.me/share/url?url=https://t.me/Premium_RenameBot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"ʏᴏᴜ  ᴡɪʟʟ  ɢᴇᴛ  100 ᴍʙ  ᴇxᴛʀᴀ  ᴀᴛ  ᴇᴠᴇʀʏ  ʀᴇꜰᴇʀ :- https://t.me/Premium_RenameBot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
