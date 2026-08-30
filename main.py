from datetime import date
import json

expenses=[]

def display_expenses():
    if not expenses:
        print("No expenses available!!!")
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
         8. Exit
         ''')
    
def search_by_category():
    print("\n=========| SEARCH by CATEGORY |=========\n")
    
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
            category_number=int(input("\nEnter category number: "))
            if category_number>=1 and category_number<=len(categories):
                actual_index=category_number-1
                selected_category=categories[actual_index]
                print(f"Selected category: {selected_category}")
                # for expense in expenses:
                #     if expense['category']==selected_category:
                #         print(f"\n-----Selected Category: '{selected_category}'-----\n")
                #         print(f"   Category: {expense['category']}")
                #         print(f"   Description: {expense['description']}")
                #         print(f"   Rs: {expense['amount']:.2f}")
                #         print(f"   Date: {expense['date']}\n")
                #     else:
                #         print(f"No expenses found for '{selected_category}'!")
                # break
                for i in expenses:
                    while i['category']==selected_category:
                        print(f"   Category: {i['category']}")
                        print(f"   Description: {i['description']}")
                        print(f"   Rs: {i['amount']:.2f}")
                        print(f"   Date: {i['date']}\n")
                        break
            else:
                print(f"Enter within {len(categories)}")
                            
        except ValueError:
            print(f"Enter integer only within {len(categories)}.")

def search_by_description():
    print("=========| SEARCH by DESCRIPTION |=========")

def filter_by_date():
    print("=========| FILTER by DATE |=========")

def back():
    print("=========| BACK |=========")
    
def add_expense():
    print("=========| ADD EXPENSE |=========\n")
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

    print(f"\n=========| SELECT CATEGORY |=========\n")
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
            c=int(input(f"\nSelect category: "))
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
    if not expenses:
        print("No expenses available to display!!!")
    else:
        print("=========| YOUR EXPENSES |=========\n")
        for number, expense_item in enumerate(expenses, start=1):
            print(f"{number}. {expense_item['category']}")
            print(f"   {expense_item['description']}")
            print(f"   Rs: {expense_item['amount']:.2f}")
            print(f"   Date: {expense_item['date']}\n")

def delete_expense():
    if not expenses:
        print("No expenses available!!!")
    else:
        print("=========| YOUR EXPENSES |=========")
        for number, expense_item in enumerate(expenses, start=1):
            print(f"{number}. {expense_item['category']}")
            print(f"   {expense_item['description']}")
            print(f"   Rs: {expense_item['amount']:.2f}")
            print(f"   Date: {expense_item['date']}\n")
            
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
            print("No expenses available!!!")
    else:
        print("=========| YOUR EXPENSES |=========")
        for number, expense_item in enumerate(expenses, start=1):
            print(f"{number}. {expense_item['category']}")
            print(f"   Description: {expense_item['description']}")
            print(f"   Rs: {expense_item['amount']:.2f}")
            print(f"   Date: {expense_item['date']}\n")
            
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
                
        while True:
            try:
                new_amount=float(input("Enter new amount (in Rs): "))
                if new_amount<=0:
                    print("Enter valid amount!")
                else:
                    expense['amount']=new_amount
                    break
            except ValueError:
                print("Not a valid amount!")
        
        print("\n=========| SELECT NEW CATEGORY |=========")
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
                new_category=int(input("Enter new category: "))
                if new_category>=1 and new_category<=len(categories):
                    actual_index=new_category-1
                    expense['category']=categories[actual_index]
                    print(f"Selected category: {categories[actual_index]}")
                    break
                else:
                    print(f"Select valid category!")
            except ValueError:
                print("Enter valid category number!")
        
        while True:
            new_description=input("Enter  new description: ").strip()
            if new_description=="":
                print("Description cannot be empty!")
            else:
                expense['description']=new_description
                break
        save_expenses()
        print("\nExpense updated successfully!!!")

def view_total():
    if not expenses:
        print("No expenses available to show total!!\n")
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
    display_expenses()
    
    print("=========| SEARCH / FILTER |=========")
    print("""
    1. Search by Category
    2. Search by Description
    3. Filter by Date
    4. Back
    """)
    
    while True:
            
        try:
            choice_2=int(input("Enter you choice: "))
            if choice_2==1:
                search_by_category()
                
            elif choice_2==2:
                search_by_description()
                
            elif choice_2==3:
                filter_by_date()
                
            elif choice_2==4:
                back()
                
        except ValueError:
            print(f"Enter inter only choice within 1 and 4!")
   
load_expenses()
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
            print("Goodbye!!!")
            break
        
        else:
            print("Oops!!! Enter choice between 1 and 8!\n")
    except ValueError:
        print("Oops!!! Enter integer(only) between 1 and 8!\n")
