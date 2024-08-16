import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Api.core.settings import Settings

router = Router()


@router.message()
async def echo(message: types.Message):
    keyboard = [
        [InlineKeyboardButton(text="Аутентификация", web_app=types.WebAppInfo(url=web_url))]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.reply('Нажмите кнопку для аутентификации.', reply_markup=reply_markup)
    # await message.reply(message.text)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    settings = Settings()
    token = settings.token.get_secret_value()
    web_url = settings.web_app_url.get_secret_value()
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    asyncio.run(main())
