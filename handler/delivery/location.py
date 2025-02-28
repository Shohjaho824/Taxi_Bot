
from aiogram import types

from aiogram.dispatcher import FSMContext
from loader import dp, bot
from utils import texts, buttons
from utils.state import Delivery
from services import getUserCart, getUser

@dp.message_handler(content_types=['location'], state=Delivery.location)
async def delivery_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    user_cart = getUserCart(user_id)
    user = getUser(user_id)

    phone = user['phone']
    name = user['name']
    username = message.from_user.username or 'User'
    
    product_name = user_cart[0]['product']['name']
    price = user_cart[0]['product']['price']
    if user_cart and 'product' in user_cart[0] and 'count' in user_cart[0]['product']:
        count = user_cart[0]['product']['count']
    else:
        count = 0

    
    await bot.send_message(
        chat_id=-4593145391,
        text=texts.user_product(
        username=username,
        phone=phone,
        name=name,
        product_name=product_name,
        price=price,
        count=count   
        )
    )
    
    
    if user:
        await message.answer(f"Salom, {user['name']}! Buyurtmangiz qabul qilindi.")
    else:
        await message.answer("Foydalanuvchi topilmadi.")
