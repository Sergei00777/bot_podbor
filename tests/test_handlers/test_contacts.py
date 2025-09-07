import pytest
from unittest.mock import AsyncMock
from handlers.contacts import contacts
from telegram.constants import ParseMode


# Локальные фикстуры
@pytest.fixture
def mock_update():
    update = AsyncMock()
    update.message = AsyncMock()
    update.message.text = "Контакты"
    update.message.reply_text = AsyncMock()
    return update


@pytest.fixture
def mock_context():
    context = AsyncMock()
    context.user_data = {}
    return context


@pytest.mark.asyncio
async def test_contacts(mock_update, mock_context):
    await contacts(mock_update, mock_context)

    mock_update.message.reply_text.assert_called_once()
    args, kwargs = mock_update.message.reply_text.call_args

    assert "Контакты ProAuto Иркутск" in kwargs['text']
    assert "Мобильный офис" in kwargs['text']
    assert kwargs['parse_mode'] == ParseMode.HTML
    assert kwargs['disable_web_page_preview'] == True