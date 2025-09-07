from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode
import logging

logger = logging.getLogger(__name__)


async def ai_assistant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"AI Assistant triggered with text: {update.message.text}")

    text = (
        "🤖 <b>Привет! Я твой личный помощник по подбору автомобилей!</b>\n\n"
        "Задай мне любой вопрос, и я постараюсь помочь:\n\n"
        "🚗 <b>Я могу ответить на:</b>\n"
        "• Какой автомобиль лучше для города/семьи/поездок?\n"
        "• На что обращать внимание при осмотре б/у авто?\n"
        "• Какие марки самые надежные?\n"
        "• Сколько стоит обслуживание разных марок?\n"
        "• Как проверить юридическую чистоту?\n"
        "• Что важно знать при покупке первого авто?\n\n"
        "💡 <b>Просто напиши свой вопрос ниже ↓</b>\n"
        "Я использую базу знаний о автомобилях и помогу сделать правильный выбор!"
    )

    await update.message.reply_text(
        text=text,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def get_ai_assistant_handlers():
    return [MessageHandler(filters.Regex("^AI Ассистент$"), ai_assistant)]