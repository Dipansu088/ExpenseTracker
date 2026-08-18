expenses=[]
def menu():
    print("==============| EXPENSE TRACKER |==============")
    print('''         
         1. Add Expense
         2. View Expenses
         3. Delete Expense
         4. View Total
         5. View Summary
         6. Exit
         ''')
    
def add_expense():
    print("=========| ADD EXPENSE |=========")
    amount=float(input("Enter amount (in Rs): "))
    category=input('''Enter category (Example: Food, Transport, Shopping, Entertainment, Bills): ''')
    description=input('''Enter description (Examples: Lunch, Bus, ticket, New shirt, Movie, Electricity bill): ''')
    expenses.append({
        "amount":amount,
        "category":category,
        "description":description
    })
    print("Expense added successfully!")
    
def view_expenses():
    if not expenses:
        print("No expenses available!!!")
    else:
        print("=========| YOUR EXPENSES |=========")
        for number, expense_item in enumerate(expenses, start=1):
            print(f'''{number}. {expense_item['category']}
    {expense_item['description']}
    Rs: {expense_item['amount']}''')

def delete_expense():
    if not expenses:
        print("No expenses available!!!")
    else:
        print("=========| YOUR EXPENSES |=========")
        for number, expense_item in enumerate(expenses, start=1):
            print(f'''{number}. {expense_item['category']}
    {expense_item['description']}
    {expense_item['amount']}''')
        
        n=int(input("Enter the expense number to delete: "))
        if n>=1 and n<=len(expenses):
            actual_index=n-1
            deleted_expense=expenses.pop(actual_index)
            print(f"Expense {deleted_expense} deleted successfully!!")
        else:
            print(f"OOPS! Enter expense number within {len(expenses)}")

def view_total():
    if not expenses:
        print("No expenses available to show total!!")
    else:
        total=0
        for i in expenses:
            total=total+i['amount']
        print(f"Your total expense is: Rs {total}")

def view_summary():
    if not expenses:
        print("No expenses available for summary!")
    else:
        summary={}
        for i in expenses:
            category=i['category']
            amount=i['amount']
            if category in summary:
                summary[category] = summary[category]+amount
            else:
                summary[category]=amount
        print("=========| EXPENSE SUMMARY |=========")
        for category,total in summary.items():
            print(f"{category}: Rs {total}")
   
while True:    
    menu()
    try:
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Add Expense Selected")
            add_expense()
            
        elif choice==2:
            print("View Expense Selected")
            view_expenses()
            
        elif choice==3:
            print("Delete Expense Selected")
            delete_expense()
            
        elif choice==4:
            print("View Total Selected")
            view_total()
            
        elif choice==5:
            print("View Summary Selected")
            view_summary()
            
        elif choice==6:
            print("Goodbye!!!")
            break
        
        else:
            print("Oops!!! Enter choice between 1 and 6!")
    except ValueError:
        print("Oops!!! Enter integer between 1 and 6!")
