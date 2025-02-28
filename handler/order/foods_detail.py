from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import texts, buttons
from services import getProductDetail
from utils.state import Product




@dp.message_handler(content_types=['text'], state=Product.product_detail)
async def order(message: Message, state: FSMContext):
    product_name = message.text
    product = getProductDetail(product_name)
    
    await state.update_data({
        'product_name': product_name
    })

    
    if product:
        name = product['name']
        price = product['price']
        description = product['description']
        image_id = product['image_id']

        await message.answer_photo(
            photo=image_id,
            caption=texts.product_text(
                name=name,
                price=price,
                description=description,
            ),
            reply_markup=buttons.COUNT
        )

        await Product.count.set()
    else:
        await message.answer("Bu categoryda hech narsa yo'q")
    

