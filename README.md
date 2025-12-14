# Expense Manager CLI

A **simple command-line expense tracker** built with Python.  
Track your daily expenses, view, add, and edit them easily. Data is stored locally in **JSON format**.

---

## Features

- ✅ **Add Expense** – Add a new expense with amount, category, description, and date.  
- ✅ **View Expenses** – See a list of all your expenses in a readable format.  
- ✅ **Change Expense** – Update any field of an existing expense using its ID.  
- ✅ **Save Data** – All expenses are stored in a JSON file for persistent storage.

---

## Expense Data Structure

Each expense is stored with the following fields:

| Field       | Type    | Description                    |
|-------------|---------|--------------------------------|
| `expense_id` | int     | Unique identifier for expense  |
| `amount`    | float   | Expense amount                 |
| `category`  | string  | Expense category (e.g., Food) |
| `description` | string | Short description of expense  |
| `date`      | string  | Date of expense (DD-MM-YYYY)  |

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/sandeep-balot008/ExpenseTracker.git
cd ExpenseTracker
```

2. **Install dependencies** (if any). For this project, Python's standard library is enough.  
Make sure you have **Python 3.x** installed.

---

## Usage

Run the program:

```bash
python main.py
```

You will see a menu like this:

```
--- Expense Tracker ---
1. Add Expense
2. View Expenses
3. Change Expense
4. Exit
```

- **Add Expense:** Enter details like amount, category, description, and date.  
- **View Expenses:** Display all saved expenses.  
- **Change Expense:** Update a specific expense by its ID.  
- **Exit:** Save and exit the program.

---

## File Structure

```
ExpenseTracker/
├── main.py           # Main program
├── expense_manager.py  # Functions for adding, viewing, and changing expenses
├── file_handler.py     # Functions for saving and loading JSON data
├── expenses.json       # JSON file storing expense data
└── README.md
```

---

## Future Features

- Delete an expense  
- Search/filter expenses by category, date, or amount  
- Export expenses to CSV or Excel  
- Add summaries and analytics  
