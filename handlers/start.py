from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from keyboards.main_menu import get_main_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = get_main_keyboard()
    await update.message.reply_text(
        "Добро пожаловать в автоподбор Иркутск! 🚗\nВыберите опцию:",
        reply_markup=reply_markup
    )

def get_start_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("menu", start)
    ]