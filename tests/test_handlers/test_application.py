import pytest
from unittest.mock import AsyncMock
from handlers.contacts import contacts
from telegram.constants import ParseMode


@pytest.mark.asyncio
async def test_contacts():
    # Создаем моки вручную
    mock_update = AsyncMock()
    mock_update.message = AsyncMock()
    mock_update.message.text = "Контакты"
    mock_update.message.reply_text = AsyncMock()

    mock_context = AsyncMock()
    mock_context.user_data = {}

    # Вызываем функцию
    await contacts(mock_update, mock_context)

    # Проверяем результаты
    mock_update.message.reply_text.assert_called_once()
    args, kwargs = mock_update.message.reply_text.call_args

    assert "Контакты ProAuto Иркутск" in kwargs['text']
    assert "Мобильный офис" in kwargs['text']
    assert kwargs['parse_mode'] == ParseMode.HTML
    assert kwargs['disable_web_page_preview'] == True