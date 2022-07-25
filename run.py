import logging

from aiogram import executor
from loader import dp


logging.basicConfig(level=logging.INFO)

async def on_sturtup(dispatcher):
    import hendlers

    hendlers.setup(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_sturtup)
