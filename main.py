
from expense_manager import add_expense, view_expenses, change_expense
from file_handler import load_data, save_data

expenses = load_data()

def menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Change Expense")
    print("4. exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)
        save_data(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        expense_Id = int(input("expense_Id"))
        change_expense(expenses,expense_Id)
        save_data(expenses)
    elif choice == "4":
        save_data(expenses)
        print("goodbye!")
        break
    else:

        print("Invalide choice!")
