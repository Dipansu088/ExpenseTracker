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
    while True:
        amt=input("Enter amount (in Rs): ")
        try:
            amount=float(amt)
            if amount<=0:
                print("Enter valid amount.")
            else:
                break
        except ValueError:
            print("Not a valid amount!")

    print("=========| SELECT CATEGORY |=========")
    categories=[
        
        'Food',
        'Transport',
        'Shopping',
        'Entertainment',
        'Bills',
        'Education'
        
          ]
    
    while True:
        
        for number, category_name in enumerate(categories, start=1):
                print(f"{number}. {category_name}")
        try:
            c=int(input("Select category: "))
            if c>=1 and c<=len(categories):
                category=categories[c-1]
                print(f"Selected category: {category}")
                break
            else:
                print("Select a valid category!")
            
        except ValueError:
            print("Enter valid category number!")
    
    
    while True:
        description=input('''Enter description (Examples: Lunch, Bus, ticket, New shirt, Movie, Electricity bill): ''').strip()
        if description=='':
            print("Description cannot be empty!")
        else:
            break
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
        print("=========| YOUR EXPENSES |=========\n")
        for number, expense_item in enumerate(expenses, start=1):
            print(f"{number}. {expense_item['category']}")
            print(f"   {expense_item['description']}")
            print(f"   Rs: {expense_item['amount']:.2f}\n")

def delete_expense():
    if not expenses:
        print("No expenses available!!!")
    else:
        print("=========| YOUR EXPENSES |=========")
        for number, expense_item in enumerate(expenses, start=1):
            for number, expense_item in enumerate(expenses, start=1):
                print(f"{number}. {expense_item['category']}")
                print(f"   {expense_item['description']}")
                print(f"   Rs: {expense_item['amount']:.2f}\n")
            
        while True:
            try:
                n=int(input("Enter the expense number to delete: "))
                if n<=0:
                    print("Enter integer greater than 0 only.")
                else:
                    if n>=1 and n<=len(expenses):
                        actual_index=n-1
                        deleted_expense=expenses.pop(actual_index)
                        print(f"Expense deleted successfully!\n")
                        print(f"Category: {deleted_expense["category"]}")
                        print(f"Description: {deleted_expense["description"]}")
                        print(f"Amount: {deleted_expense["amount"]}\n")
                        break
                    else:
                        print(f"OOPS! Enter expense number within {len(expenses)}")
            except ValueError:
                print("Enter integer only!")

def view_total():
    if not expenses:
        print("No expenses available to show total!!")
    else:
        total=0
        for i in expenses:
            total=total+i['amount']
        print(f"Your total expense is: Rs {total:.2f}")

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
            print(f"{category}: Rs {total:.2f}")
   
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
