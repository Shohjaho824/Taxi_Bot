from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    name = State()
    phone = State()
    
    
class Product(StatesGroup):
    category = State()
    product_detail = State()
    count = State()
    
    
    
class Delivery(StatesGroup):
    location = State()