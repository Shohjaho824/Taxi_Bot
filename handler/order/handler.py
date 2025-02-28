from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from services import getCategory
from utils.state import Product

@dp.message_handler(lambda message: message.text.startswith(buttons.ORDER_TITLE), state='*')
async def order(message: Message, state: FSMContext):
    category = getCategory()
    await message.answer(texts.CATEGORY, reply_markup=buttons.category_button(category))
    await Product.category.set()
    