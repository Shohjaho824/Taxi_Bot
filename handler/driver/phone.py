from aiogram.types import Message
from aiogram.dispatcher import FSMContext


from loader import dp,bot
from utils.env import ADMIN
from utils import texts
from utils.state import DRIVER
from asyncio import create_task


async def driver_handler_task(message: Message, state: FSMContext):

    phone = message.contact.phone_number

    await state.update_data({
        'phone':phone
    })

    data = await state.get_data()
    name = data.get('name')

    
    await bot.send_message(
        chat_id=ADMIN,
        text=texts.send_driver( 
            phone = phone,
            name = name,
        )
    )
    await message.answer('Tabriklayman sizning arizangiz ADMINGA yuborildi✅')
    
    await state.finish()


@dp.message_handler(content_types=('contact', 'text'), state=DRIVER.phone)
async def passenger_handler(message: Message, state: FSMContext):
    await create_task(driver_handler_task(message, state))