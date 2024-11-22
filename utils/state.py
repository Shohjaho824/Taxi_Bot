from aiogram.dispatcher.filters.state import State, StatesGroup


class Passenger(StatesGroup):
    count = State()
    location = State()
    phone = State()
    check = State()

class MAIL(StatesGroup):
    location = State()
    phone = State()

class DRIVER(StatesGroup):
    name = State()
    phone = State()










