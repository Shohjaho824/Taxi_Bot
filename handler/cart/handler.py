from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import texts, buttons
from services import getUserCart

@dp.message_handler(lambda message: message.text == buttons.CART, state="*")
async def user_cart(message: Message, state: FSMContext):
    user_id = message.from_user.id

    user_cart = getUserCart(user_id)

    for item in user_cart:
        product_name = item['product']['name']
        product_price = item['product']['price']

        await message.answer(
            texts.cart_text(
                product_name=product_name,
                product_price=product_price,
            )
        )

    await message.answer("Tanlang:", reply_markup=buttons.USER_CART)
