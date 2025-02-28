from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from utils.state import Product
from services import createCartUser


@dp.message_handler(content_types=['text'], state=Product.count)
async def count_handler(message: Message, state: FSMContext):
    count = message.text
    user_id = message.from_user.id
    data = await state.get_data()
    product_name = data.get('product_name')

    cart = {
        'user_id': user_id,
        'product_name': product_name,
        'count': count
    }
    createCartUser(cart)

    await message.answer("Sizning savatchangiz:", reply_markup=buttons.USER_CART)
