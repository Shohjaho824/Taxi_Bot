from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from services import getProduct
from utils.state import Product


@dp.message_handler(content_types=['text'], state=Product.category)
async def order(message: Message, state: FSMContext):
    category = message.text
    product = getProduct(category)
    if product:        
        await message.answer(texts.PRODUCT_SELECT, reply_markup=buttons.product_button(product))

    else:
        await message.answer(text='Mahsulot topilmadi🧐')
        
        
    await Product.product_detail.set()
