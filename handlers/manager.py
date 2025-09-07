from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode


async def contact_manager(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👨‍💼 *Свяжитесь с нашим менеджером*\n\n"
        "Мы готовы ответить на все ваши вопросы и помочь с подбором автомобиля\\!\n\n"
        "📍 *Контакт менеджера:*\n"
        "➖➖➖➖➖➖➖➖➖➖\n"
        "🔹 *Сергей* \\- специалист по подбору авто\n"
        "📱 [Написать в Telegram](https://t\\.me/PSergei007)\n"
        "⏰ *Время работы:* 9:00 \\- 21:00\n"
        "📞 *Телефон:* \\+7 \\(914\\) 123\\-45\\-67\n\n"
        "💬 *Не стесняйтесь обращаться\\!* \n"
        "Мы поможем найти автомобиль вашей мечты\\! 🚗💨"
    )

    await update.message.reply_text(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True
    )


def get_manager_handlers():
    return [MessageHandler(filters.Regex("^Связаться с менеджером$"), contact_manager)]