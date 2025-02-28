from loader import dp
from utils import texts, buttons
from services import getUser
from utils.state import Register
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    """
    Botning asosiy / start Funksiyasi.
    """
    user_id = message.from_user.id 
    
    user = getUser(user_id)
    
    if user:
        await message.answer(texts.START, reply_markup=buttons.MENU)
    else:
        await message.answer(texts.NAME)
        await Register.name.set()