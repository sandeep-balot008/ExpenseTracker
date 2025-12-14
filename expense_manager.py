def add_expense(expenses):
    expense_Id = int(input("Expense_Id: "))
    amount = float(input("Amount: "))
    category = input("Category: ")
    description = input("Description: ")
    date = input("Date (DD-MM-YYYY): ")

    expense = {
        "expense_Id": expense_Id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
        }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expense found.")
    
        return

    print("sr.no.| ID |    date    | category | amount | description ")

    for i, exp in enumerate(expenses):
        print(f"{i+1}.    |  {exp['expense_Id']} | {exp['date']} | {exp['category']}   | {exp['amount']} | {exp['description']}")


def change_expense(expenses, expense_Id):
    for expense in expenses:
        if expense["expense_Id"] == expense_Id:
           
           print("\npress Enter to keep the current value\n")

           new_amount = input(f"Amount({expense['amount']}): ")
           new_category = input(f"Category({expense['category']}): ")
           new_description = input(f"Description({expense['description']}): ")
           new_date = input(f"Date({expense['date']}): ")

           if new_amount:
               expense["amount"] = float(new_amount)
           if new_category:
               expense["category"] = new_category
           if new_description:
               expense["description"] = new_description
           if new_date:
               expense["date"] = new_date

           print("Expense update!")
           return
    print("Expense ID not found.")
               
   
