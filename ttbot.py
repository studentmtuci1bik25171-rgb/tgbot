import asyncio
import logging
import aiohttp
import os
from telethon import TelegramClient, events, connection

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('TELEGRAM_TOKEN')
proxy_ip = os.getenv('PROXY_IP')
proxy_port = os.getenv('PROXY_PORT')
proxy_token = os.getenv('PROXY_TOKEN')

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient(
    'bot', api_id, api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=(proxy_ip, proxy_port, proxy_token)
)

@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    await event.reply('Howdy, how are you doing?')

@bot.on(events.NewMessage(pattern='(^cat[s]?$|puss)'))
async def cats(event):
    await event.reply('Cats is here 😺', file='data/cats.jpg')

@bot.on(events.NewMessage)
async def echo_all(event):
    await event.reply(event.text)

if __name__ == '__main__':
    bot.start()
    bot.run_until_disconnected()