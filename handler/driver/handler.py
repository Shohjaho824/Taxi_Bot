from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp
from utils import texts, buttons
from utils.state import DRIVER

@dp.message_handler(lambda message: message.text.startswith(buttons.DRIVER), state="*")
async def check_handler(message: Message, state: FSMContext):
    
    await message.answer(texts.DRIVER_HANDLER, reply_markup=buttons.NAME)
    await DRIVER.name.set()