# 💰 Expense Tracker (CLI)

A simple, no-dependency command-line application to track your daily expenses, manage a monthly budget, and export your spending history — all built in pure Python using JSON for storage.

## ✨ Features

- **Add Expenses** — Log an amount, pick from 12 built-in categories, and add a short description (date is stamped automatically).
- **View Expenses** — See all logged expenses in a clean, numbered list.
- **Edit / Delete Expenses** — Update or remove any expense by its number.
- **View Total** — Get the sum of all expenses recorded.
- **View Summary** — See a category-wise breakdown of total spending.
- **Search & Filter** — Find expenses by:
  - Category
  - Description (partial match, case-insensitive)
  - Exact date (`DD-MM-YYYY`)
- **Monthly Budget Tracking** — Set a budget and check your status (spent, remaining, % used) with warnings when you're nearing or over budget.
- **Clear All Expenses** — Wipe your expense history with a confirmation prompt.
- **Export to CSV** — Save all expenses to `expenses.csv` for use in Excel, Google Sheets, etc.
- **Persistent Storage** — All data is saved automatically to `expenses.json` and `budget.json`, so your data survives between runs.

## 📂 Categories

```
Transfers, Groceries, Transport, Bills & recharges, Entertainment,
Shopping, Food & dining, Miscellaneous, Medical, Personal, Logistics, Travel
```

## 🛠️ Requirements

- Python 3.7 or higher
- No external libraries required (uses only Python's standard library: `datetime`, `json`, `csv`)

## 🚀 Getting Started

1. Clone or download this repository.
2. Run the script:

   ```bash
   python expense_tracker.py
   ```

3. Use the on-screen menu to navigate:

   ```
   1. Add Expense
   2. View Expenses
   3. Delete Expense
   4. Edit Expense
   5. View Total
   6. View Summary
   7. Search/Filter
   8. Set Monthly Budget
   9. View Budget Status
   10. Clear All Expenses
   11. Export to CSV
   12. Exit
   ```

## 📁 Files Generated

| File             | Purpose                                   |
|------------------|--------------------------------------------|
| `expenses.json`  | Stores all your logged expenses            |
| `budget.json`    | Stores your set monthly budget             |
| `expenses.csv`   | Generated when you export your expenses    |

These files are created automatically in the same folder as the script the first time you use the relevant feature.

## 💡 Example Workflow

1. Choose **1 (Add Expense)** → enter amount → pick a category → add a description.
2. Choose **8 (Set Monthly Budget)** → enter your budget for the month.
3. Choose **9 (View Budget Status)** → track how much you've spent vs. your budget.
4. Choose **11 (Export to CSV)** → get a spreadsheet-ready copy of your expenses.

## 🔮 Possible Future Improvements

- Recurring/monthly-repeating expenses
- Multi-currency support
- Data visualization (charts of spending by category)
- Import expenses from CSV/bank statements
- Undo for delete/clear actions

## 📄 License

Feel free to use, modify, and share this project for personal or educational purposes.
