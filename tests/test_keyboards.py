from keyboards.main_menu import get_main_keyboard


def test_main_keyboard():
    keyboard = get_main_keyboard()

    assert keyboard is not None
    assert hasattr(keyboard, 'keyboard')
    assert len(keyboard.keyboard) == 4  # 6 rows of buttons

    # Check that all expected buttons are present
    button_texts = []
    for row in keyboard.keyboard:
        for button in row:
            button_texts.append(button.text)

    expected_buttons = [
        "Каталог автомобилей",
        "Оставить заявку на подбор",
        "Чек-лист",
        "AI Ассистент",
        "О нас / Услуги и цены",
        "Контакты",
        "Связаться с менеджером"
    ]

    for expected_button in expected_buttons:
        assert expected_button in button_texts