from aiogram.types import Message
from aiogram.dispatcher import FSMContext


from loader import dp
from utils import texts, buttons
from utils.state import DRIVER
from .handler import DRIVER

from asyncio import create_task



async def driver_handler_task(message: Message, state: FSMContext):
    
    name = message.text
    
    
    await state.update_data({
        'name': name
    })
    
    await message.answer(texts.PHONE, reply_markup=buttons.PHONE)
    
    await DRIVER.phone.set()
    
    
    
@dp.message_handler(content_types=['text'], state=DRIVER.name)
async def passenger_handler(message: Message, state: FSMContext):
    await create_task(driver_handler_task(message, state))