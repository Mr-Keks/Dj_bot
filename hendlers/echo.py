from aiogram import types
from loader import dp


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Вибач, я можу виконувати лише одну команду з пошуку")