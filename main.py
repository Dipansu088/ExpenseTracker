from datetime import date, datetime
import json

expenses=[]

CATEGORIES=[
            
            'Transfers',
            'Groceries',
            'Transport',
            'Bills & recharges',
            'Entertainment',
            'Shopping',
            'Food & dining',
            'Miscellaneous',
            'Medical',
            'Personal',
            'Logistics',
            'Travel'
    
              ]

def display_expenses():
    if not expenses:
        print("\nNo expenses available!!!\n")
    else:
        print("\n=========| YOUR EXPENSES |=========\n")
        for number, expense_item in enumerate(expenses, start=1):
            print(f"{number}. {expense_item['category']}")
            print(f"   {expense_item['description']}")
            print(f"   Rs: {expense_item['amount']:.2f}")
            print(f"   Date: {expense_item['date']}\n")

def load_expenses():
    global expenses
    try:
        with open("expenses.json","r") as file:
            expenses=json.load(file)
    except FileNotFoundError:
        expenses=[]
        
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
        
def load_budget():
    try:
        with open("budget.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return 0
    
def save_budget(budget):
    with open("budget.json", "w") as file:
        json.dump(budget, file, indent=4)

def menu():
    print("==============| EXPENSE TRACKER |==============")
    print('''         
         1. Add Expense
         2. View Expenses
         3. Delete Expense
         4. Edit Expense
         5. View Total
         6. View Summary
         7. Search/Filter
         8. Set Monthly Budget
         9. View Budget Status
         10. Exit
         ''')
    
def get_valid_amount():
    while True:
        amount_input=input("Enter amount (in Rs): ")
        try:
            amount=float(amount_input)
            if amount<=0:
                print("Enter valid amount.")
            else:
                return amount
        except ValueError:
            print("Not a valid amount!")
            
def get_current_month_expenses():
    current_month=date.today().strftime("%m-%Y")
    total=0
    
    for expense in expenses:
        expense_month=expense['date'][3:]
        
        if expense_month==current_month:
            total+=expense['amount']
    
    return total
    
def search_by_category():
    print("\n=========| SEARCH by CATEGORY |=========\n")
                
    while True:
        
        for number, category_name in enumerate(CATEGORIES, start=1):
            print(f"{number}. {category_name}")
            
        try:
            category_number=int(input("\nEnter category number: "))
            if category_number>=1 and category_number<=len(CATEGORIES):
                actual_index=category_number-1
                selected_category=CATEGORIES[actual_index]
                print(f"Selected category: {selected_category}")
                
                found=False
                print(f"\n-----Selected Category: '{selected_category}'-----\n")
                for expense in expenses:
                    if expense['category']==selected_category:
                        print(f"   Category: {expense['category']}")
                        print(f"   Description: {expense['description']}")
                        print(f"   Rs: {expense['amount']:.2f}")
                        print(f"   Date: {expense['date']}\n")
                        found=True
                if not found:
                    print(f"No expenses found for '{selected_category}'!")
                break
            else:
                print(f"Enter within {len(CATEGORIES)}")
                            
        except ValueError:
            print(f"Enter integer only within {len(CATEGORIES)}.")

def search_by_description():
    print("\n=========| SEARCH by DESCRIPTION |=========\n")
    
    while True:
            search_description=input("Enter description you want to search by: ").strip()
            
            found=False
            for expense in expenses:
                if search_description.lower() in expense['description'].lower():
                    print(f"   Category: {expense['category']}")
                    print(f"   Description: {expense['description']}")
                    print(f"   Rs: {expense['amount']:.2f}")
                    print(f"   Date: {expense['date']}\n")
                    found=True
                    
            if not found:
                print(f"No expenses of {search_description} available.")
            break

def validate_date(date_input):
    try:
        datetime.strptime(date_input, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def filter_by_date():
    print("\n=========| FILTER by DATE |=========\n")

    while True:
        search_date=input("Enter the date to search (DD-MM-YYYY): ").strip()
        if validate_date(search_date):
            break
        print("Invalid date! Please enter a valid date in DD-MM-YYYY format.")
    
    found=False
    for expense in expenses:
        if expense['date']==search_date:
            print(f"   Category: {expense['category']}")
            print(f"   Description: {expense['description']}")
            print(f"   Rs: {expense['amount']:.2f}")
            print(f"   Date: {expense['date']}\n")
            found=True
    if not found:
        print(f"No expense of {search_date} available!")
    
def add_expense():
    print("=========| ADD EXPENSE |=========\n")
    amount=get_valid_amount()

    print(f"\n=========| SELECT CATEGORY |=========\n")
    
    while True:
        
        for number, category_name in enumerate(CATEGORIES, start=1):
                print(f"{number}. {category_name}")
        try:
            c=int(input(f"\nSelect category: "))
            if c>=1 and c<=len(CATEGORIES):
                category=CATEGORIES[c-1]
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
    
    expense_date=date.today().strftime("%d-%m-%Y")
    
    expenses.append({
        "amount":amount,
    "category":category,
    "description":description,
    "date":expense_date
    })
    save_expenses()
    print("Expense added successfully!\n")
    
def view_expenses():
    display_expenses()

def delete_expense():
    
    if not expenses:
        print("\nNo expenses available to display!!!\n")
        return
    
    display_expenses()
            
    while True:
        try:
            n=int(input("Enter the expense number to delete: "))
            if n<=0:
                print("Enter integer greater than 0 only.")
            else:
                if n>=1 and n<=len(expenses):
                    actual_index=n-1
                    deleted_expense=expenses.pop(actual_index)
                    save_expenses()
                    print(f"Expense deleted successfully!\n")
                    print(f"Category: {deleted_expense['category']}")
                    print(f"Description: {deleted_expense['description']}")
                    print(f"Amount: Rs.{deleted_expense['amount']:.2f}")
                    print(f"Date: {deleted_expense['date']}\n")
                    break
                else:
                    print(f"OOPS! Enter expense number within {len(expenses)}")
        except ValueError:
            print("Enter integer only!")

def edit_expense():
    
    if not expenses:
        print("\nNo expenses available to display!!!\n")
        return
    
    display_expenses()
            
    while True:
        try:
            n=int(input("Enter expense number to edit: "))
            if n>=1 and n<=len(expenses):
                actual_index=n-1
                expense=expenses[actual_index]
                print(f"\n-----Selected Expense: -----\n")
                print(f"   Category: {expense['category']}")
                print(f"   Description: {expense['description']}")
                print(f"   Rs: {expense['amount']:.2f}")
                print(f"   Date: {expense['date']}\n")
                break
            else:
                print(f"Enter expense number between 1 and {len(expenses)}")
        except ValueError:
            print("Enter integer only!")
    
    new_amount=get_valid_amount()
    expense['amount']=new_amount
        
    print("\n=========| SELECT NEW CATEGORY |=========")
        
    while True:
        for number, category_name in enumerate(CATEGORIES, start=1):
            print(f"{number}. {category_name}")
        try:
            new_category=int(input("Enter new category: "))
            if new_category>=1 and new_category<=len(CATEGORIES):
                actual_index=new_category-1
                expense['category']=CATEGORIES[actual_index]
                print(f"Selected category: {CATEGORIES[actual_index]}")
                break
            else:
                print(f"Select valid category!")
        except ValueError:
            print("Enter valid category number!")
        
    while True:
        new_description=input("Enter new description: ").strip()
        if new_description=="":
            print("Description cannot be empty!")
        else:
            expense['description']=new_description
            break
    save_expenses()
    print("\nExpense updated successfully!!!\n")

def view_total():
    if not expenses:
        print("\nNo expenses available to show total!!\n")
    else:
        total=0
        for i in expenses:
            total=total+i['amount']
        print(f"Your total expense: Rs {total:.2f}\n")

def view_summary():
    if not expenses:
        print("No expenses available for summary!\n")
    else:
        summary={}
        for i in expenses:
            category=i['category']
            amount=i['amount']
            if category in summary:
                summary[category] = summary[category]+amount
            else:
                summary[category]=amount
        print("=========| EXPENSE SUMMARY |=========\n")
        for category,total in summary.items():
            print(f"{category}: Rs {total:.2f}")
            
            
def search_filter():

    while True:
        if not expenses:
                print("No expenses available!")
                return
            
        print("\n=========| SEARCH / FILTER |=========")
        print("""
            1. Search by Category
            2. Search by Description
            3. Filter by Date
            4. Back
            """)
            
        try:
            choice_2=int(input("Enter you choice: "))
            if choice_2==1:
                search_by_category()
                
            elif choice_2==2:
                search_by_description()
                
            elif choice_2==3:
                filter_by_date()
                
            elif choice_2==4:
                break
            
            else:
                print("Enter choice between 1 and 4!")
                
        except ValueError:
            print(f"Enter inter only choice within 1 and 4!")
            
def set_budget():
    global budget
    while True:
        print("\n=========| SET BUDGET |=========\n")
        try:
            new_budget=float(input("Enter new budget: "))
            if new_budget<=0:
                print("Budget must be greater than 0.")
            else:
                budget=new_budget
                save_budget(budget)
                print(f"\nMonthly budget was set to Rs: {budget:.2f}\n")
                break
        except ValueError:
            print("Enter valid amount/budget!")
            
def view_budget_status():
    
    if budget<=0:
        print("\nNo monthly budget has been set!\n")
        return
    
    current_month_expenses=get_current_month_expenses()
    remaining= budget - current_month_expenses
    percentage_used=(current_month_expenses/budget)*100
    
    print("\n=========| BUDGET STATUS |=========\n")
    print(f"Monthly Budget : Rs {budget:.2f}")
    print(f"Spent          : Rs {current_month_expenses:.2f}")
    print(f"Remaining      : Rs {remaining:.2f}")
    print(f"Budget Used    : {percentage_used:.2f}%")
    
    if percentage_used>=100:
        print(f"WARNING!!! You have exceeded your monthly budget!!!")
    elif percentage_used>=80:
        print(f"WARNING!!! You are nearing your monthly budget!!")
    else:
        print(f"You are within your monthly budget!")
        
    print()
   
load_expenses()
budget=load_budget()

while True:    
    menu()
    try:
        choice=int(input(f"Enter your choice: "))
        if choice==1:
            add_expense()
            
        elif choice==2:
            view_expenses()
            
        elif choice==3:
            delete_expense()
        
        elif choice==4:
            edit_expense()
            
        elif choice==5:
            view_total()
            
        elif choice==6:
            view_summary()
            
        elif choice==7:
            search_filter()
            
        elif choice==8:
            set_budget()
            
        
        elif choice==9:
            view_budget_status()
            
        elif choice==10:
            print("Goodbye!!!")
            break
        
        else:
            print("Oops!!! Enter choice between 1 and 10!\n")
            
    except ValueError:
        print("Oops!!! Enter integer(only) between 1 and 10!\n")
