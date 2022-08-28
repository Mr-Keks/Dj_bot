from aiogram.dispatcher.filters.state import State, StatesGroup


class Download(StatesGroup):
    begin = State()
    url = State()
