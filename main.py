from telethon import events, TelegramClient
from os import getenv
from droplink import getLink
from dotenv import load_dotenv

load_dotenv()
# Get your own values from my.telegram.org
api_id = getenv('API_ID')
api_hash = getenv('API_HASH')
token = getenv('TOKEN')

bot = TelegramClient('main', api_id, api_hash).start(bot_token=token)


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("Hi! [{}]({})".format(event.sender.first_name, event.sender_id))


@bot.on(events.NewMessage(pattern="/link"))
async def link(event):
    try:
        link = event.text.split(' ', 1)[1]
    except IndexError:
        await event.reply("`Usage: /link <link>`")
        return
    res = getLink(link)
    if res is None:
        await event.reply("Error!")
        return
    await event.reply(res)


bot.run_until_disconnected()


