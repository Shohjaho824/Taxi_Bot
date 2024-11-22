from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from utils.state import MAIL

@dp.message_handler(lambda message: message.text.startswith(buttons.MAIL), state='*')
async def passenger_handler(message: Message, state: FSMContext):

    await message.answer(texts.MAIL_HANDLER, reply_markup=buttons.LOCATION)
    await MAIL.location.set()