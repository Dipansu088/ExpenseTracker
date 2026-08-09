expenses=[]
def menu():
    print("========== EXPENSE TRACKER ==========")
    print('''         
         1. Add Expense
         2. View Expenses
         3. Delete Expense
         4. View Total
         5. View Summary
         6. Exit
         ''')
   
while True:    
    menu()
    try:
        choice=int(input("Enter your choice: "))
        if choice==1:
            print("Add Expense Selected")
        elif choice==2:
            print("View Expense Selected")
        elif choice==3:
            print("Delete Expense Selected")
        elif choice==4:
            print("View Total Selected")
        elif choice==5:
            print("View Summary Selected")
        elif choice==6:
            print("Goodbye!!!")
            break
        else:
            print("Oops!!! Enter choice between 1 and 6!")
    except ValueError:
        print("Oops!!! Enter integer between 1 and 6!")
