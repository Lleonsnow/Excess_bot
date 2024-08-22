import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from Api.core.settings import Settings

bot_router = Router()
api_router = APIRouter()


class AuthData(BaseModel):
    username: str
    password: str


# @api_router.get("/")
# async def root():
#     print("API is working")


@api_router.post("/webhook")
async def webhook(auth_data: AuthData):
    print(auth_data)
    print("Webhook is working")


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


async def main():
    await asyncio.gather(start_api(), start_bot())


if __name__ == '__main__':
    api = FastAPI()
    api.include_router(api_router)
    api.add_middleware(CORSMiddleware, allow_origins=["*"], allow_headers=["*"], allow_methods=["*"], allow_credentials=True)
    settings = Settings()
    token = settings.token.get_secret_value()
    web_url = settings.web_app_url.get_secret_value()
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(bot_router)
    asyncio.run(main())
