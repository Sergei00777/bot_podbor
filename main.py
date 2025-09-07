import logging
from telegram.ext import Application
from config import TOKEN
from handlers.start import get_start_handlers
from handlers.about import get_about_handlers
from handlers.contacts import get_contacts_handlers
from handlers.manager import get_manager_handlers
from handlers.application import get_application_handlers
from handlers.checklist import get_checklist_handlers
from handlers.ai_assistant import get_ai_assistant_handlers
from handlers.ai_questions import get_ai_questions_handlers
from handlers.unknown import get_unknown_handlers

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики в правильном порядке
    handlers = []
    handlers.extend(get_start_handlers())
    handlers.extend(get_about_handlers())
    handlers.extend(get_contacts_handlers())
    handlers.extend(get_manager_handlers())
    handlers.extend(get_application_handlers())
    handlers.extend(get_checklist_handlers())
    handlers.extend(get_ai_assistant_handlers())  # Обработчик кнопки AI Ассистент
    handlers.extend(get_ai_questions_handlers())  # Обработчик вопросов к AI
    handlers.extend(get_unknown_handlers())  # Unknown должен быть последним

    for handler in handlers:
        application.add_handler(handler)

    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main()