from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup



MAIN_BACK = 'Ortga'


PASSENGER = "Yolovchi🧑🏻"
DRIVER = "Taksi bolish🚖"
MAIL = "Pochta yuborish✉️"


BASE_BACK = 'Ortga'




START = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=MAIL)
        ],
        [
            KeyboardButton(text=DRIVER),
            KeyboardButton(text=PASSENGER),
        ]
    ],


    resize_keyboard=True

)



ONE = '1️⃣ kishi'
TWO = '2️⃣ kishi'
THREE = '3️⃣ kishi'
FOUR = '4️⃣ kishi'


BACK = 'Ortga❌'

COUNT = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text=ONE),
            KeyboardButton(text=TWO),
        ],

        [
            KeyboardButton(text=THREE),
            KeyboardButton(text=FOUR),
        ],

    
        [
            KeyboardButton(text=BASE_BACK),
        ]

    ],

    resize_keyboard=True
)



B_T = 'Beshariq-Toshket📌'
T_B = 'Toshkent-Beshariq📌'

LOCATION = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=B_T),
                KeyboardButton(text=T_B),
            ],
            [
                KeyboardButton(text=BASE_BACK)
            ]
        ],
        resize_keyboard=True
)



PHONE_NUMBER = 'Telefon raqam yuborish📞'


PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=PHONE_NUMBER, request_contact=True)
        ],
        [
            KeyboardButton(text=BASE_BACK)
        ]
    ],
    resize_keyboard=True
)

CHECK = 'Tasdiqlash✅'
CANCEL = 'Bekor qilish❌'


SEND_GROUP = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=CHECK)
        ],
        [
            KeyboardButton(text=CANCEL)
        ]
    ],
    resize_keyboard=True
)





B_T = 'Beshariq-Toshket📌'
T_B = 'Toshkent-Beshariq📌'

LOCATION = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=B_T),
                KeyboardButton(text=T_B),
            ],
            [
                KeyboardButton(text=BASE_BACK)
            ]
        ],
        resize_keyboard=True
)


PHONE_NUMBER = 'Telefon raqam yuborish☎️'


PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=PHONE_NUMBER, request_contact=True)
        ],
        [
            KeyboardButton(text=BACK)
        ]
    ],
    resize_keyboard=True
)
    

NAME = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BACK)
        ]
    ],
    resize_keyboard=True
)











