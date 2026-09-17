from unittest.mock import patch
from expense_tracker import add_expense, data_validation

#@patch('builtins.input', side_effect=["twenty four", "7/8/26", "123"])
#def test_add_expense(mock_input, capsys):
#   add_expense()          #the failed function return None in the assertion to prevent that
#
#    captured = capsys.readrouter()
 #   assert "Enter Valid Amount in Numbers" in captured.out   #captured-out :Contains everything your program printed using print()

def test_amount_validation():
    #assert data_validation("twenty three thousand", "15/09/26", "healthcare")  == False
    #assert data_validation("2000", "20/09/25", "education") ==  True
    #assert data_validation("-5000", "15/10/20", "education") == False
    pass
def test_category_validation():
    #assert data_validation("5000", "26/02/22", "") == False
    #assert data_validation("5000", "26/10/12", "enterntainment") == True
    pass
def test_date_validation():
    #assert data_validation("6500", "", "self-care") == False
    #assert data_validation("4500", "15/09/20", "self_care") == True
    pass
    