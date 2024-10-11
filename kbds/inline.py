from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

async def create_buttons(time_slots):
    keyboard = InlineKeyboardBuilder()
    for start_slot, end_slot in time_slots:
        keyboard.add(InlineKeyboardButton(text=f'{start_slot} - {end_slot}', callback_data='button_1'))
    return keyboard.adjust(3,).as_markup()
