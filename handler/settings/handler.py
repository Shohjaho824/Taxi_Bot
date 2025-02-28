from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons

@dp.message_handler(lambda message: message.text == buttons.SETTINGS)
async def settings(message: Message, state: FSMContext):
    await message.answer(texts.SETTINGS_INFO, reply_markup=buttons.SETTINGS_INFO)
