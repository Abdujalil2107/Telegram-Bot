from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram import F
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters.command import Command
import asyncio

API_TOKEN = '7860585465:AAFABcUAfCmjJwZxxyeoldmhGrkBec-3l8I'

async def main():
    session = AiohttpSession()
    bot = Bot(token=API_TOKEN, session=session)
    dp = Dispatcher()

    @dp.message(Command(commands=["start"]))
    async def start_handler(message: Message):
        await message.answer("Salom Bot ishga tushdi !!!")

    @dp.message(F.text)
    async def echo_handler(message: Message):
        await message.answer(f"Siz yuborgan xabar: {message.text}")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
