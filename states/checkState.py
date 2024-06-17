from aiogram.dispatcher.filters.state import State, StatesGroup


class Check(StatesGroup):
    name = State()
    size = State()
    price = State()
    number = State()
    type_sell = State()
    status = State()
