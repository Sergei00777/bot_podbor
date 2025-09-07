import pytest
from unittest.mock import patch, MagicMock
from main import main


def test_main_imports():
    """Test that all imports work correctly"""
    # This test just ensures that the main module can be imported without errors
    try:
        import main
        assert True
    except ImportError as e:
        pytest.fail(f"Import failed: {e}")


@patch('main.Application.builder')
def test_main_function(mock_builder):
    """Test that main function sets up the application correctly"""
    mock_app = MagicMock()
    mock_builder.return_value.token.return_value.build.return_value = mock_app

    # Mock all handler functions to avoid actual imports
    with patch('main.get_start_handlers'), \
            patch('main.get_about_handlers'), \
            patch('main.get_contacts_handlers'), \
            patch('main.get_manager_handlers'), \
            patch('main.get_application_handlers'), \
            patch('main.get_checklist_handlers'), \
            patch('main.get_ai_assistant_handlers'), \
            patch('main.get_ai_questions_handlers'), \
            patch('main.get_unknown_handlers'):
        # Call main function
        main()

        # Verify that application was built and run
        mock_builder.assert_called_once()
        mock_app.run_polling.assert_called_once()