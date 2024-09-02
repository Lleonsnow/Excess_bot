import asyncio
import os
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.core.settings import Settings

bot_router = Router()


@bot_router.message()
async def echo(message: types.Message):
    keyboard = [
        [InlineKeyboardButton(text="Аутентификация", web_app=types.WebAppInfo(url=web_url))]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.reply('Нажмите кнопку для аутентификации.', reply_markup=reply_markup)
    # await message.reply(message.text)


async def start_bot():
    await dp.start_polling(bot)


settings = Settings()
token = settings.token.get_secret_value()
web_url = settings.web_app_url.get_secret_value()
bot = Bot(token=token)
dp = Dispatcher()
dp.include_router(bot_router)
asyncio.run(start_bot())
