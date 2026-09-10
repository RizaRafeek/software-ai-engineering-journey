from unittest.mock import patch
from expense_tracker import add_expense

@patch('builtins.input', side_effect=["twenty four", "7/8/26", "123"])
def test_add_expense(mock_input, capsys):
    add_expense()          #the failed function return None in the assertion to prevent that

    captured = capsys.readrouter()
    assert "Enter Valid Amount in Numbers" in captured.out   #captured-out :Contains everything your program printed using print()