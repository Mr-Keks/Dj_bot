from aiogram.dispatcher.filters.state import State, StatesGroup

'''
1. натиск кнопки завантажити
2. введення урл
3. повертання файлу
'''


class Download(StatesGroup):
    begin = State()
    url = State()
    file = State()
