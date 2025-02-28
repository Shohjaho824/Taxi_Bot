from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(content_types=['photo'], state='*')
async def file_id(message: Message, state: FSMContext):
    file_id = message.photo[0].file_id
    await message.answer(file_id)