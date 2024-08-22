import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from fastapi import FastAPI, APIRouter

from Api.core.settings import Settings

bot_router = Router()
api_router = APIRouter()


@api_router.get("/")
async def root():
    ...


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


async def start_api():
    import uvicorn
    config = uvicorn.Config(app=api, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == '__main__':
    api = FastAPI()
    api.include_router(api_router)
    settings = Settings()
    token = settings.token.get_secret_value()
    web_url = settings.web_app_url.get_secret_value()
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(bot_router)
    asyncio.gather(start_api(), start_bot())
