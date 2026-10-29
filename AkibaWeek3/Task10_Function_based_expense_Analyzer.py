
Expenses=[]
def Add_Expense():
    description=input("Enter description: ")
    category=input("Enter category(Food,Bills,Transport,and Others) choose from those 4 categories: ")
    amount=int(input("Enter amount: "))
    Expenses.append({
        "description": description,
        "category": category,
        "amount":amount
    })
    return f"Expense added succesfully! \n{Expenses}"


def Total_expense():
    totalExpense=0
    for expense in Expenses:
        totalExpense+=expense["amount"]
    return totalExpense

def Category_Spending():
    categorySpending=0
    categoryspend=input("Which category spending do you wanna know? ")
    categoryspend.lower()
    for expense in Expenses:
        if expense["category"]==categoryspend:
            categorySpending+=expense["amount"]
    return f"{categoryspend} category spending is: {categorySpending} ETB"

    
def Threshold():
    ThreAmount=int(input(" Enter the Threshold amount you want: "))
    AboveThreshold=[]
    for expense in Expenses:
        if expense["amount"]>ThreAmount:
            AboveThreshold.append(
                {
                    "description": expense["description"],
                    "category": expense["category"],
                    "amount": expense["amount"]
                }
            )
    return f"List of Expenses Above Threshold: \n{AboveThreshold}"


def spending_report():
    print(f"============================\n       SPENDING REPORT \n============================")
    spending_food=0
    spending_Transport=0
    spending_Bills=0
    spending_others=0
    for expense in Expenses:
        if expense["category"]=="Food":
            spending_food +=expense["amount"]
        elif expense["category"]=="Transport":
            spending_Transport +=expense["amount"]
        elif expense["category"]=="Bills":
            spending_Bills+=expense["amount"]
        else:
            spending_others+=expense["amount"]
    print(f"Food = {spending_food} ETB")
    print(f"Transport = {spending_Transport} ETB")
    print(f"Bills = {spending_Bills} ETB")
    print(f"Others = {spending_others} ETB")
    
    return spending_food, spending_Transport, spending_others,spending_Bills
def Largest_Lowest_Spending(total,spending_food,spending_Transport,spending_Bills,spending_others):
    spendings = {
        "Food": spending_food,
        "Transport": spending_Transport,
        "Bills": spending_Bills,
        "Others": spending_others
    }
    percentageOfFoodSpending=round((spending_food/total)*100, 2)
    percentageOfTransportSpending=round((spending_Transport/total)*100, 2)
    percentageOfBillSpending=round((spending_Bills/total)*100, 2)
    percentageOfOtherSpendings=round((spending_others/total)*100, 2)

    
    highest_category = max(spendings, key=spendings.get) # type: ignore
    lowest_category = min(spendings, key=spendings.get) # type: ignore
    return f"Out of total spendings:\nFoods Spending is{percentageOfFoodSpending}% \nBills Spendings is{percentageOfBillSpending}% \nTransports spendings is {percentageOfTransportSpending}% \nOther Spendings is {percentageOfOtherSpendings}% \n\nYour Highest spending is {highest_category} and Your lowest spending is {lowest_category}"
    

def Options():
    while True:
        print(f"1. Add expenses \n2. Total Expense \n3. Spending by category \n4. Expenses Above Threshold \n5. Highest and lowest spendings. \n6. Spending Report. \n7. Exit")
        option=input("Choose option: ")
        if option =="1":
            print(Add_Expense())
        elif option == "2":
            print(f"The Total Expense is: {Total_expense()}ETB")
        elif option == "3":
            print(Category_Spending())
        elif option == "4":
            print(Threshold())
        elif option == "5":
            total = Total_expense()
            spending_food, spending_bills, spending_others, spending_transport = spending_report()
            print(Largest_Lowest_Spending(total, spending_food, spending_transport, spending_bills, spending_others))
        elif option == "6":
            spending_report()
        elif option == "7":
            break 
        else:
            print("Enter valid Option!")

Options()