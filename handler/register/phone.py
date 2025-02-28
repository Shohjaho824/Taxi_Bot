from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from utils.state import Register
from services import createUser

@dp.message_handler(content_types=['text', 'contact'], state=Register.phone)
async def phone_handler(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text

    data = await state.get_data()
    name = data.get('name')

    user_id = message.from_user.id

    user = {
        'user_id': user_id,
        'name': name,
        'phone': phone
    }

    createUser(user)

    await message.answer(texts.SUCCESS)
