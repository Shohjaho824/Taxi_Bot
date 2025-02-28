from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from utils.state import Delivery


@dp.message_handler(lambda message: message.text == buttons.DELIVERY)
async def delivery_handler(message: Message, state: FSMContext):
    await message.answer(texts.LOCATION, reply_markup=buttons.LOCATION)
    
    await Delivery.location.set()
