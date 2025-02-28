START = \
"""
Assalomu alaykum!
"""

NAME = \
"""
Ismingizni kiriting!
"""


PHONE = \
"""
Telefon raqamingizni kiriting!
"""

SUCCESS = \
"""
Bosh menyu.
"""

CATEGORY = \
"""
Mahsulotni tanlang!
"""

def product_text(**kwargs):
    product = ''
    product += f"Mahsulot nomi: {kwargs['name']}\n\n"
    product += f"Mahsulot narxi: {kwargs['price']}\n\n"
    product += f"Mahsuot haqida fikirlar: {kwargs['description']}\n"
    return product


PRODUCT_SELECT = \
"""
Mahsulotni turini tanlang!
"""

PRODUCT_BASKET_SUCCESS = \
"""
Bu categoryda hech narsa yo'q.
"""

def cart_text(**kwargs):
    cart = ""

    cart += "Mahsulotingiz:\n\n"
    cart += f"📛Nomi: {kwargs['product_name']}\n\n"
    cart += f"💲Narxi: {kwargs['product_price']}\n"

    return cart


LOCATION = "Iltimos, manzilingizni yuboring."



def user_product(**kwargs):
    order = (
        f"📩 Telegram: @{kwargs.get('username', 'Noma’lum')}\n"
        f"👤 Ism: {kwargs.get('name', 'Noma’lum')}\n"
        f"📞 Telefon: {kwargs.get('phone', 'Noma’lum')}\n"
        f"📦 Mahsulot: {kwargs.get('product_name', 'Noma’lum')}\n"
        f"💰 Narxi: {kwargs.get('price', 'Noma’lum')}\n"
        f"🔢 Soni: {kwargs.get('count', 'Noma’lum')}\n"
    )
    return order


SETTINGS_INFO = \
"""
Ma'lumotlarni o'zgartirish uchun quyidagi tugmalardan foydalanishingiz mumkin.
"""