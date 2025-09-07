from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Игнорируем сообщения, которые являются командами меню
    menu_commands = [
        "Каталог автомобилей",
        "Оставить заявку на подбор",
        "Чек-лист",
        "AI Ассистент",
        "О нас / Услуги и цены",
        "Контакты",
        "Связаться с менеджером"
    ]

    if update.message.text not in menu_commands:
        await update.message.reply_text("Извините, я не понимаю эту команду. Используйте кнопки меню.")


def get_unknown_handlers():
    return [MessageHandler(filters.TEXT & ~filters.COMMAND, unknown)]