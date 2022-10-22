from telebot.async_telebot import AsyncTeleBot
import dotenv
import asyncio
import os
import sys
sys.path.insert(0, 'S:\\CryptoCurrencyBot\\Parser')

import parser


dotenv.load_dotenv()

bot = AsyncTeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, "Привет! Я помогу тебе следить за курсами нужных тебе криптовалют к нужной валюте! Напиши мне следующим сообщением нужную крипту и валюту, а я пришлю ее курс. К примеру BTC USD")


@bot.message_handler(func=lambda message: True)
async def send_currency(message):
    coin = parser.Coin(message.text.split()[0])
    await bot.send_message(message.chat.id, f"Сейчас цена на {coin.coin} в валюте {message.text.split()[1]}: {coin.get_currency(message.text.split()[1])}")


asyncio.run(bot.polling())
