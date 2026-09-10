from datetime import date, datetime
import json
import csv
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

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

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def display_expenses():
    
    connection=get_connection()
    
    try:
        cursor=connection.cursor()
        cursor.execute("""
                       SELECT id, amount, category, description, expense_date 
                       FROM expenses 
                       ORDER BY id;
                       """)
        
        expenses=cursor.fetchall()
        
        if not expenses:
            print("\nNo expenses available to display!!\n")
            return
        
        print("\n=========| YOUR EXPENSES |=========\n")
        
        for expense in expenses:
            expense_id=expense[0]
            amount=expense[1]
            category=expense[2]
            description=expense[3]
            expense_date=expense[4]
            
            print(f"{expense_id}: {category}")
            print(f"   {description}")
            print(f"   Rs: {amount:.2f}")
            print(f"   Date: {expense_date.strftime('%d-%m-%Y')}\n")
            
    except Exception as e:
        print(f"Falied to load expenses: {e}\n")
        
    finally:
        cursor.close()
        connection.close()
        
def load_expenses():
    global expenses
    
    try:
        with open("expenses.json", "r") as file:
            data=json.load(file)
            
        if not isinstance(data, list):
            print("Warning: expenses.json does not contain a valid expense list.")
            expenses=[]
            return
        
        valid_expenses=[]
        for expense in data:
            if validate_expenses(expense):
                valid_expenses.append(expense)
            else:
                print("Warning: Invalid expense found and skipped.")
                
        expenses=valid_expenses
        
    except FileNotFoundError:
        expenses=[]
    except json.JSONDecodeError:
        print("Warning: expenses.json is corrupted.")
        print("Starting with an empty expense list.\n")
        expenses = []
    except OSError as error:
        print(f"Warning: Could not read expenses.json: {error}")
        expenses = []
        
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
        
def save_expenses():
    temp_file="expenses.json.tmp"
    
    try:
        with open(temp_file, "w") as file:
            json.dump(expenses, file, indent=4)
        os.replace(temp_file, "expenses.json")
        
    except OSError as error:
        print(f"Error: Could not save expenses: {error}")
        
        if os.path.exists(temp_file):
            os.remove(temp_file)
        
def load_budget():
    try:
        with open("budget.json", "r") as file:
            budget=json.load(file)
        if isinstance(budget, bool):
            print("WARNING!!! Invalid budget value found!")
            return 0
        if not isinstance(budget, (int, float)):
            print("WARNING!!! Invalid budget value found!")
            return 0
        if budget<=0:
            print("Budget must be greater than 0 !!!")
            return 0
        
        return budget
    except FileNotFoundError:
        return 0
    except json.JSONDecodeError:
        print("Warning: budget.json is corrupted.")
        print("Starting without a monthly budget.\n")
        return 0
    except OSError as error:
        print(f"WARNING! Could not read budget.json: {error}")
        return 0
        
def save_budget(budget):
    temp_file="budget.json.tmp"
    
    try:
        with open("temp_file", "w") as file:
            json.dump(budget, file, indent=4)
        os.replace(temp_file, "budget.json")
    except OSError as error:
        print(f"Could not save budget: {error}")
        
        if os.path.exists(temp_file):
            os.remove(temp_file)

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
         10. Clear All Expenses
         11. Export to CSV
         12. Exit
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
        if not validate_expenses(expenses):
            continue
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
                    print(f"\n   Category: {expense['category']}")
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
    
def validate_expenses(expense):
    
    if not isinstance(expense, dict):
        return False
    
    required_fields=[
        "amount",
        "category",
        "description",
        "date"
    ]
    
    for field in required_fields:
        if field not in expense:
            return False
    
    amount=expense['amount']
    category=expense['category']
    description=expense['description']
    expense_date=expense['date']
    
    if not isinstance(amount, (float, int)):
        return False
    if isinstance(amount, bool):
        return False
    if not isinstance(category, str) or category not in CATEGORIES:
        return False
    if not isinstance(description, str) or description.strip()=="":
        return False
    if not isinstance(expense_date, str) or not validate_date(expense_date):
        return False
    return True

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
    
    expense_date=date.today()
    
    connection=get_connection()
    
    try:
        cursor=connection.cursor()
        cursor.execute("""
                       INSERT INTO expenses(amount, category, description, expense_date)
                       VALUES(%s,%s,%s,%s);""",
                       (amount, category, description, expense_date))
        
        connection.commit()
        print("Expense added successfully!!!\n")
        
    except Exception as e:
        connection.rollback()
        print(f"Failed to add expense: {e}\n")
        
    finally:
        cursor.close()
        connection.close()
    
def view_expenses():
    display_expenses()

def delete_expense():
    
    connection=get_connection()
        
    try:
        cursor=connection.cursor()
        cursor.execute("""
                        SELECT id, amount, category, description, expense_date
                        FROM expenses
                        ORDER BY id
                        """)
        
        expenses=cursor.fetchall()
            
        if not expenses:
            print("\nNo expenses available!!!\n")
            return
            
        print("\n=========| YOUR EXPENSES |=========\n")
            
        for expense in expenses:
            expense_id=expense[0]
            amount=expense[1]
            category=expense[2]
            description=expense[3]
            expense_date=expense[4]
            
            print(f"{expense_id}. {category}")
            print(f"   {description}")
            print(f"   Rs: {amount:.2f}")
            print(f"   Date: {expense_date.strftime('%d-%m-%Y')}\n")
            
        while True:
            try:
                expense_id=int(input("Enter expense ID to delete: "))
                    
                if expense_id<=0:
                    print("Enter a valid expense ID!!")
                    continue
                    
                cursor.execute("""
                                SELECT id, category, description
                                FROM expenses
                                WHERE id=%s;
                                """,(expense_id,))
                    
                expense=cursor.fetchone()
                if expense is None:
                    print(f"\nNo expense of ID: {expense_id} found!\n")
                    continue
                    
                cursor.execute("""
                                DELETE FROM expenses
                                WHERE id=%s;
                                """,(expense_id,))
                
                connection.commit()
                    
                print(f"\nExpense '{expense[1]} - {expense[2]}' deleted successfully!!!\n")
                break
                
            except ValueError:
                print("\nEnter integer only!\n")
                    
    except Exception as e:
        connection.rollback()
        print(f"Failed to delete expense: {e}\n")
            
    finally:
        cursor.close()
        connection.close()

def edit_expense():
    
    connection=get_connection()
    
    try:
        cursor=connection.cursor()
        cursor.execute("""
                       SELECT id, amount, category, description, expense_date
                       FROM expenses
                       ORDER BY id;
                        """)
        expenses=cursor.fetchall()
        
        if not expenses:
            print("\nNo expenses available!!!")
            return
        
        print("\n=========| YOUR EXPENSES |=========\n")
        
        for expense in expenses:
            expense_id=expense[0]
            amount=expense[1]
            category=expense[2]
            description=expense[3]
            expense_date=expense[4]
            
            print(f"{expense_id}. {category}")
            print(f"   {description}")
            print(f"   Rs: {amount:.2f}")
            print(f"   Date: {expense_date.strftime('%d-%m-%Y')}\n")
            
        while True:
            try:
                expense_id=int(input("Enter expense ID you wanna edit: "))
                
                if expense_id<=0:
                    print("Enter valid ID!")
                    continue
                
                cursor.execute("""
                               SELECT id, amount, category, description, expense_date
                               FROM expenses
                               WHERE id=%s;
                               """,(expense_id,))
                
                expense=cursor.fetchone()
                
                if expense is None:
                    print(f"No expenses of ID {expense_id} found!!")
                    continue
                
                break
            
            except ValueError:
                print("Enter integer only!!")
        
        while True:
            try:
                new_amount=float(input("Enter new amount: "))
                
                if new_amount<=0:
                    print("Amount must be greater than 0...!")
                    continue
                break
            
            except ValueError:
                print("Enter valid amount!!")
                
        print("\n=========| SELECT NEW CATEGORY |=========\n")
        
        while True:
            for number, category_name in enumerate(CATEGORIES, start=1):
                print(f"{number}. {category_name}")
                
            try:
                c=int(input("\nSelect new category: "))
                
                if c>=1 and c<=len(CATEGORIES):
                    new_category=CATEGORIES[c-1]
                    break
                else:
                    print("\nSelect within the given list of categories!\n")
                    
            except ValueError:
                print("Enter a valid category(integer/number)!!!")
                
        while True:
            new_description=input("Enter new description: ").strip()
                
            if new_description=="":
                print("Description cannot be empty!")
            else:
                break
                
        while True:
            new_date=input("Enter new date (DD-MM-YYYY): ").strip()
            
            try:
                new_date=datetime.strptime(new_date, "%d-%m-%Y").date()
                break
            
            except ValueError:
                print("Enter data in DD-MM-YYYY formate!!")
                
        cursor.execute("""
                       UPDATE expenses
                       SET amount=%s, category=%s, description=%s, expense_date=%s
                       WHERE id=%s;
                       """,
                       (new_amount, new_category, new_description, new_date, expense_id))
        
        connection.commit()
        
        print("\nExpense updated successfully!!!\n")
        
    except Exception as e:
        connection.rollback()
        print(f"Failed to update expense: {e}\n")
        
    finally:
        cursor.close()
        connection.close()

def view_total():
    
    connection=get_connection()
    
    try:
        cursor=connection.cursor()
        cursor.execute("""
                       SELECT COALESCE(SUM(amount), 0)
                       FROM expenses;
                       """)
        total=cursor.fetchone()[0]
        
        print("\n=========| TOTAL EXPENSE |=========\n")
        print(f"Total spent: Rs: {total:.2f}\n")
        
    except Exception as e:
        print(f"\nFailed to calculate total: {e}\n")
        
    finally:
        cursor.close()
        connection.close()

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
            print("\nNo expenses available!\n")
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
                print("\nEnter choice between 1 and 4!\n")
                
        except ValueError:
            print(f"\nEnter inter only choice within 1 and 4!\n")
            
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
    
def clear_expenses():
    if not expenses:
        print("No expenses available!")
        return
            
    while True:
        choice=input("Do you really want to clear all the expenses?? Type Y/N(Yes/No): ").strip()
        if choice.lower()=='y':
            expenses.clear()
            save_expenses()
            print("All expenses cleared!!!")
            return
        elif choice.lower()=='n':
            break
        else:
            print("Enter Y or N!!")
            
def export_to_csv():
    if not expenses:
        print("No expenses available!")
        return
    
    try:
        with open("expenses.csv", "w", newline="") as file:
            fieldnames=["category", "amount", "description", "date"]
            
            writer=csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
        print("\nExpenses successfully exported to expenses.csv!\n")
        
    except OSError as error:
        print(f"\nError: Could not export expenses to CSV: {error}\n")
   
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
            clear_expenses()
            
        elif choice==11:
            export_to_csv()
            
        elif choice==12:
            print("Goodbye!!!")
            break
        
        else:
            print("Oops!!! Enter choice between 1 and 12!\n")
            
    except ValueError:
        print("Oops!!! Enter integer(only) between 1 and 12!\n")
