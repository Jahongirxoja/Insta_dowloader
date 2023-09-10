from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.from_user.id
    full_name = message.from_user.full_name
    await db.create_user(chat_id,full_name)
    await message.answer(f"Assalomu aleykum {full_name}")
