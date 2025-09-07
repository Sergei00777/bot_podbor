from telegram import KeyboardButton, ReplyKeyboardMarkup

def get_main_keyboard():
    keyboard = [
        [KeyboardButton("Каталог автомобилей")],
        [KeyboardButton("Оставить заявку на подбор"), KeyboardButton("AI Ассистент")],
        [KeyboardButton("Чек-лист"), KeyboardButton("О нас / Услуги и цены") ],
        [KeyboardButton("Контакты"), KeyboardButton("Связаться с менеджером")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)