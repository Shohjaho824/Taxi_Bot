from aiogram.types import Message
from aiogram.dispatcher import FSMContext



from loader import dp,bot
from utils.env import GROUP_ID
from utils import texts, buttons
from utils.state import MAIL
from asyncio import create_task




@dp.message_handler(content_types=('contact'), state=MAIL.phone)
async def passenger_handler_task(message: Message, state: FSMContext):

    phone = message.contact.phone_number

    await state.update_data({
        'phone':phone
    })

    data = await state.get_data()
    count = data.get('count')
    location = data.get('location')

    
    await bot.send_message(
        chat_id=GROUP_ID,
        text=texts.send_mail( 
            count = count,
            phone = phone,
            location = location,
        )
    )
    await message.answer('Tabriklayman sizning arizangiz ADMINGA yuborildi✅')
    
    await state.finish()


@dp.message_handler(content_types=('contact', 'text'), state=MAIL.phone)
async def passenger_handler(message: Message, state: FSMContext):
    if message.text in [buttons.BASE_BACK]:
         await message.answer(texts.LOCATION, reply_markup=buttons.LOCATION)
         await MAIL.location.set()
    else:
        await create_task(passenger_handler_task(message, state))