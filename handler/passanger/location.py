from aiogram.types import Message
from aiogram.dispatcher import FSMContext


from loader import dp
from utils import texts, buttons
from utils.state import Passenger
from .handler import passenger_handler

from asyncio import create_task



async def passenger_handler_task(message: Message, state: FSMContext):
    
    location = message.text
    
    
    await state.update_data({
        'location': location
    })
    
    await message.answer(texts.PHONE, reply_markup=buttons.PHONE)
    
    await Passenger.phone.set()
    
    
    
@dp.message_handler(content_types=['text'], state=Passenger.location)
async def passenger_handler(message: Message, state: FSMContext):
    if message.text in [buttons.BACK]:
        await message.answer(texts.PASSENGER_HANDLER, reply_markup=buttons.COUNT)
        await Passenger.count.set()
    else:
        await create_task(passenger_handler_task(message, state))