from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,  InlineKeyboardMarkup



PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Yuborish', request_contact=True)
        ]
    ],
    resize_keyboard=True
)

ORDER_TITLE = "📦 Buyurtma berish"
CART = "🛒 Savat"
CONTACT = "📞 Biz bilan aloqa"
SETTINGS = "⚙️ Sozlamalar"

MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=ORDER_TITLE),
            KeyboardButton(text=CART)
        ],
        [
            KeyboardButton(text=CONTACT),
            KeyboardButton(text=SETTINGS)
        ],
    ],
    resize_keyboard=True
)



def category_button(categories):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        button = KeyboardButton(text=category['name'])
        keyboard.add(button)
    return keyboard



COUNT = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
        ],
        [
            KeyboardButton(text='4'),
            KeyboardButton(text='5'),
            KeyboardButton(text='6'),
        ],
        [
            KeyboardButton(text='7'),
            KeyboardButton(text='8'),
            KeyboardButton(text='9'),
        ],
        [
            KeyboardButton(text='Ortga'),
            KeyboardButton(text="/start")
        ]
    ],
    resize_keyboard=True
)

def product_button(products):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    for product in products:
        button = (KeyboardButton(text=product['name']))
        keyboard.add(button)

    return keyboard



BACK_TITLE = "🔙 Ortga"
DELIVERY = "🚚 Yetkazib berish"

USER_CART = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=DELIVERY)],
        [KeyboardButton(text=BACK_TITLE)]
    ],
    resize_keyboard=True
)



LOCATION = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzilni yuborish", request_location=True)
        ],
        [
            KeyboardButton(text='/start')
        ]
    ],
    resize_keyboard=True
)



NAME_UPDATE = "Ismni o'zgartirish"
PHONE_UPDATE = "Telefon raqamini yangilash"

SETTINGS_INFO = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=NAME_UPDATE),
            KeyboardButton(text=PHONE_UPDATE),
        ],
        [
            KeyboardButton(text=BACK_TITLE)
        ],
    ],
    resize_keyboard=True
)


NAME_UPDATE = "Ismni o'zgartirish"
PHONE_UPDATE = "Telefon raqamini yangilash"

SETTINGS_INFO = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=NAME_UPDATE),
            KeyboardButton(text=PHONE_UPDATE),
        ],
        [
            KeyboardButton(text=BACK_TITLE),
            KeyboardButton(text="/start")
        ],
    ],
    resize_keyboard=True
)
