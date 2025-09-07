from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode

# База знаний с ответами на частые вопросы
AI_KNOWLEDGE_BASE = {
    "город": "Для города рекомендую компактные хэтчбеки: Hyundai Solaris, Kia Rio, Volkswagen Polo. Они маневренные, экономичные и удобные для парковки.",
    "внедорожник": "Для внедорожников смотрите Toyota RAV4, Hyundai Tucson, Kia Sportage. Надежные, комфортные и с хорошей проходимостью.",
    "бюджет": "В бюджетном сегменте отлично себя показывают: Lada Vesta, Renault Logan, Hyundai Solaris. Недорогие в обслуживании и ремонте.",
    "надежность": "Самые надежные марки: Toyota, Honda, Mazda. Из корейских - Hyundai и Kia. Немецкие требуют больше внимания к обслуживанию.",
    "б у": "При покупке б/у авто обязательно: проверьте историю, сделайте диагностику, осмотрите кузов на предмет коррозии, проверьте документы.",
    "подбор": "Наш сервис подбора включает: поиск по параметрам, юридическую проверку, техническую диагностику, сопровождение сделки. Стоимость от 10 000 руб.",
    "стоимость": "Стоимость подбора автомобиля - от 10 000 рублей. Зависит от сложности поиска и дополнительных услуг.",
    "гарантия": "Даем гарантию на подобранный автомобиль - 14 дней на юридическую чистоту и 7 дней на техническое состояние.",
}


async def handle_ai_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text.lower()

    # Проверяем, не является ли это командой меню
    menu_commands = ["каталог автомобилей", "оставить заявку", "чек-лист",
                     "ai ассистент", "о нас", "услуги и цены", "контакты", "связаться с менеджером"]

    if any(cmd in user_question for cmd in menu_commands):
        return  # Пропускаем обработку, это команда меню

    # Поиск подходящего ответа в базе знаний
    response = "🤖 <b>AI Ассистент:</b>\n\n"

    found_answer = False
    for keyword, answer in AI_KNOWLEDGE_BASE.items():
        if keyword in user_question:
            response += f"{answer}\n\n"
            found_answer = True

    if not found_answer:
        response += (
            "К сожалению, я не нашел точного ответа на ваш вопрос.\n\n"
            "Рекомендую:\n"
            "• Оставить заявку на подбор - наш специалист проконсультирует подробнее\n"
            "• Связаться с менеджером для индивидуальной консультации\n"
            "• Посмотреть наш чек-лист осмотра автомобилей\n\n"
            "💡 <i>Я постоянно учусь и скоро смогу отвечать на больше вопросов!</i>"
        )
    else:
        response += "💡 <i>Нужна более подробная консультация? Оставьте заявку или свяжитесь с менеджером!</i>"

    await update.message.reply_text(
        text=response,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )


def get_ai_questions_handlers():
    return [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ai_question)]