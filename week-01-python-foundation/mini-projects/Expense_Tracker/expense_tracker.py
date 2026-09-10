file_name = "expense.txt"

def load_file():
    expense_list =[]
    try:
        with open(file_name, 'r') as file:
            for line in file:
                amount, date, category = line.strip().split(' : ')
                expense = {
                    'amount': float(amount),
                    'date': date,
                    'category': category
                }
                expense_list.append(expense)
    except FileNotFoundError:
        print("File not found,Starting with an empty expense list.")
    return expense_list

def save_file(new_expense):
    with open(file_name, 'a') as file:
        file.write(f"{new_expense['amount']} : {new_expense['date']} : {new_expense['category']}\n")

def data_validation(amount, date, category):
    try:
        amount = float(amount)
    except ValueError:
        print("Enter Valid Amount in Numbers")
        return False
    if amount <= 0:
        print("Invalid amount: Please enter a positive value for the expense")
        return False
    if date  == "":
        print("Invalid date")
        return False
    if category  == "":
        print("Enter the category")
        return False
    return True

def add_expense():
    expense = input("Enter the expense amount:") 
    date = input("Enter the date of the expense (yyyy-mm-dd): ")
    category = input("Enter the category of the expense:")
    data_validation_result = data_validation(expense, date, category)
    if data_validation_result:
        new_expense = {
            "amount" : expense,
            "date" : date,
            "category" : category
        }
        save_file(new_expense)

def list_expenses():
    expenses = load_file()
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Date: {expense['date']}, Category: {expense['category']}")

def search_expenses():
    expenses = load_file()
    expense_to_search =input("Enter the expense category to search for")
    for expense in expenses:
        if expense["category"] == expense_to_search:
            print(f"Expense found: {expense}")


def calculate_total():
    expenses = load_file()
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: {total}")


if __name__ == "__main__":
    print("Enter your choice:")
    print('1.Add Expense')
    print('2.List expenses')
    print('3.Search Expense')
    print('4.Calculate Total')
    print('5.Exit')

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        if choice == '2':
            list_expenses()
        elif choice == '3':
            search_expenses()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice: Please select valid option(1-5)")

