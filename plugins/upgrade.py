"""lokaman"""
import random
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters
from Script import script
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/sonali_sahaibot")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/sonali_sahaibot"),
        			InlineKeyboardButton("Paytm",url = "https://t.me/sonali_sahaibot")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = script.UPGRADE_PLAN_TXT,reply_markup = keybord)
