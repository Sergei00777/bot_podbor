from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters, ConversationHandler, CommandHandler
from utils.states import NAME, PHONE, CAR_MODEL, BUDGET, COMMENT
from config import ADMIN_CHAT_ID
from keyboards.main_menu import get_main_keyboard


async def start_application(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚗 <b>Отлично! Давайте оформим заявку на подбор авто</b>\n\nДля начала введите ваше имя:\n\n"
        "❌ <i>Для отмены введите /cancel в любой момент</i>",
        parse_mode='HTML',
        reply_markup=get_main_keyboard()
    )
    return NAME


async def process_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/cancel':
        return await cancel(update, context)

    context.user_data['name'] = update.message.text
    await update.message.reply_text(
        "📞 Теперь введите ваш номер телефона:\n\n"
        "❌ <i>Для отмены введите /cancel</i>",
        parse_mode='HTML'
    )
    return PHONE


async def process_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/cancel':
        return await cancel(update, context)

    context.user_data['phone'] = update.message.text
    await update.message.reply_text(
        "🔍 Какой автомобиль ищете? (Марка, модель, год):\n\n"
        "❌ <i>Для отмены введите /cancel</i>",
        parse_mode='HTML'
    )
    return CAR_MODEL


async def process_car_model(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/cancel':
        return await cancel(update, context)

    context.user_data['car_model'] = update.message.text
    await update.message.reply_text(
        "💰 Укажите ваш бюджет (в рублях):\n\n"
        "❌ <i>Для отмены введите /cancel</i>",
        parse_mode='HTML'
    )
    return BUDGET


async def process_budget(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/cancel':
        return await cancel(update, context)

    context.user_data['budget'] = update.message.text
    await update.message.reply_text(
        "💬 Дополнительные пожелания или комментарии:\n\n"
        "❌ <i>Для отмены введите /cancel</i>",
        parse_mode='HTML'
    )
    return COMMENT


async def process_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == '/cancel':
        return await cancel(update, context)

    context.user_data['comment'] = update.message.text

    # Формируем заявку для отправки
    application_text = (
        "🚗 <b>НОВАЯ ЗАЯВКА НА ПОДБОР АВТО</b>\n\n"
        f"👤 <b>Имя:</b> {context.user_data['name']}\n"
        f"📞 <b>Телефон:</b> {context.user_data['phone']}\n"
        f"🔍 <b>Автомобиль:</b> {context.user_data['car_model']}\n"
        f"💰 <b>Бюджет:</b> {context.user_data['budget']} руб.\n"
        f"💬 <b>Комментарий:</b> {context.user_data['comment']}\n\n"
        f"🆔 <b>User ID:</b> {update.message.from_user.id}\n"
        f"👤 <b>Username:</b> @{update.message.from_user.username if update.message.from_user.username else 'не указан'}"
    )

    # Отправляем заявку админу
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=application_text,
        parse_mode='HTML'
    )

    # Подтверждаем пользователю
    await update.message.reply_text(
        "✅ <b>Спасибо! Ваша заявка принята!</b>\n\n"
        "Наш менеджер свяжется с вами в ближайшее время для уточнения деталей.\n\n"
        "🚗 Хорошего дня!",
        parse_mode='HTML',
        reply_markup=get_main_keyboard()
    )

    # Очищаем данные
    context.user_data.clear()
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❌ Заявка отменена.",
        reply_markup=get_main_keyboard()
    )
    context.user_data.clear()
    return ConversationHandler.END


def get_application_handlers():
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^Оставить заявку на подбор$"), start_application)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_phone)],
            CAR_MODEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_car_model)],
            BUDGET: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_budget)],
            COMMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_comment)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    return [conv_handler]