from dotenv import find_dotenv, load_dotenv
import os
from aiogram import Bot, Dispatcher,types, F
import asyncio
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from time_into_intervals import generate_time_slots

load_dotenv(find_dotenv())
API_TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ))
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Привет")

@dp.message(F.text)
async def cmd_start(message: types.Message):
    times=message.text.split('-')
    a= await generate_time_slots(times[0],times[1])
    await message.answer(text="выберите время", reply_markup=a)



# Запуск бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())