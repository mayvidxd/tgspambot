import os
try:
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
except:
    os.system('pip install telethon')
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types

bot = input("Please Enter Session Name:")
print('enter your api id')
api_id = input()
print('enter your api hash')
api_hash = input()
client = TelegramClient(bot,api_id,api_hash)
client.start()
@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.raw_text == "hi":
        await event.reply("hello")
        await event.reply("hi")


client.run_until_disconnected()




#Remember api_id Is int and no need to put "" or ''
#Remember api_hash Is string and need to put " in first and end it
#find another Commands and requests from tl.telethon.dev