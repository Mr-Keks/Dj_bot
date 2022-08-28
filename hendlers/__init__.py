from aiogram import Dispatcher

from .main import get_url, find_music
from .start import start_work
from .echo import bot_echo


def setup(dp: Dispatcher):
    # start
    dp.register_message_handler(start_work)

    # main
    dp.register_message_handler(get_url)
    dp.register_message_handler(find_music)

    # echo
    dp.register_message_handler(bot_echo)
