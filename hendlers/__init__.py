from aiogram import Dispatcher

from .main import get_url, find_music
from .start import start_work


def setup(dp: Dispatcher):
    dp.register_message_handler(start_work)
    dp.register_message_handler(get_url)
    dp.register_message_handler(find_music)
