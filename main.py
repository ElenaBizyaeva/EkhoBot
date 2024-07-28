import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import config

API_TOKEN = config.token


# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Замените 'YOUR_BOT_TOKEN' на токен, полученный от @BotFather
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я эхо-бот. Отправь мне сообщение, и я его повторю.")


# Обработчик всех текстовых сообщений
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)


# Функция запуска бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
