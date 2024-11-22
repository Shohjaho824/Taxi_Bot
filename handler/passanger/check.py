from aiogram. types import Message
from aiogram.dispatcher import FSMContext


from loader import dp, bot
from utils import buttons, texts
from utils.env import GROUP_ID







@dp.message_handler(lambda message: message.text.startswith(buttons.CHECK), state="*")
async def check_handler(message: Message, state: FSMContext):
    
    data = await state.get_data()
    count = data.get('count')
    location = data.get('location')
    phone = data.get('phone')
    username = message.from_user.username
    
    await bot.send_message(
    chat_id=GROUP_ID,
    text=texts.send_gruop(
        count=count,
        location=location,
        phone=phone,
        username=username
    )
    )


    await message.answer('Arizangiz ADMIN ga yuborildi!')