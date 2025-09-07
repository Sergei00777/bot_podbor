from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode


async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📞 <b>Контакты ProAuto Иркутск</b>\n\n"
        "📍 <b>Город:</b> Иркутск (работаем по всему городу и области)\n\n"
        "🔹 <b>Телефон:</b> +7 (914) 123-45-67\n"
        "🔹 <b>WhatsApp/Telegram:</b> @ProAutoIrk\n"
        "🔹 <b>Email:</b> info@proauto-irk.ru\n\n"
        "🚗 <b>Мобильный офис</b>\n"
        "➖➖➖➖➖➖➖➖➖➖\n"
        "• Работаем по всему Иркутску\n"
        "• Осмотр авто производится на месте у продавца\n"
        "• Встречи с клиентами — по предварительной договорённости\n\n"
        "💡 <i>Мы сами приедем в удобное для вас место!</i>\n"
        "🕐 <b>Режим работы:</b> ежедневно с 9:00 до 21:00"
    )

    await update.message.reply_text(
        text=text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def get_contacts_handlers():
    return [MessageHandler(filters.Regex("^Контакты$"), contacts)]