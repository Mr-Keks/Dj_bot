from aiogram import types
from loader import dp
from utils.misc.throttling import rate_limit


@dp.message_handler(state=None)
@rate_limit(limit=3)
async def bot_echo(message: types.Message):
    await message.answer("Вибач, я можу виконувати лише одну команду з пошуку")
