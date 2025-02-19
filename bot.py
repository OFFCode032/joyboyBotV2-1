import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6769975697:AAEKNVPAfieMX2IiKbDIpBJxX-gr4-o1_Dk")

API_ID = int(os.environ.get("API_ID", "25123457"))

API_HASH = os.environ.get("API_HASH", "dab02224473fa37fc8c7f7c57280d9a3")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
