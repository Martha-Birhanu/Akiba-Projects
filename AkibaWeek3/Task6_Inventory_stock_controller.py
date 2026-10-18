products=[]


def AddProduct():
    name=input("Enter products name: ")
    price=float(input("Enter price: "))
    stock=int(input(f"Enter the Quantity of {name}: "))

    products.append({
        "name":name,
        "price": price,
        "stock": stock
    })

    return f"Products added succesfully!\n{products}"


def SearchProduct():
    SearchByName=input("Enter the name of product you want to check: ")
    for product in products:
        if product["name"] == SearchByName:
            return f"Yes {SearchByName} Exists!"
        else:
            return F"{SearchByName} doesn't Exist!"


def UpdatePrice():
    product_name=input("Enter the products name you want to update the price: ")

    New_price=float(input("Enter the new price: "))
    for product in products:
        if product["name"] == product_name:
            product["price"]=New_price
            return f"Price updated! \nThe new price for {product["name"]} is: {product["price"]}ETB"


def IncreaseStock():

    product_name=input("Enter the products name you want to update the stock: ")
    
    AddStock=int(input("How many stocks do you wanna add? "))
    
    for product in products:
        if product["name"] == product_name:
            product["stock"]= AddStock+product["stock"]


            return f"Stock increased! \nThe new stock for {product["name"]} is: {product["stock"]}"


def sellProduct():
    product_name=input("Enter product name: ")

    product_stock=int(input("Enter Quantity: "))

    for product in products:
        if product["name"]==product_name and product["stock"]>=product_stock:
            product["stock"] -= product_stock
            price=product["price"] * product_stock
            return f"sold {product_stock} {product_name} for {price} ETB."
        else:
            return "insufficient stock"

    return "Product not found."


def Total_Inventory():
    totalInventory=0

    for product in products:
       totalInventory+=product["price"]*product["stock"]
    return f"Total Inventory value is: {totalInventory}ETB"

def Low_Stock(threshold):
    found=False
    for product in products:
        if product["stock"]<threshold:
            print(f"product {product["name"]} has stock of {product["stock"]}")
            found=True
    if not found:
        return " There is no product with low stock!"
        


def ChooseOptions():
    while True:
        print(f"1. Add new product \n2. Search for product  \n3. Update product price  \n4. Increase stock  \n5. Sell Product \n6. Generate low stock products report   \n7. Total inventory value.  \n8. Exit")
        option=input("Choose Option: ")
        if option == "1":
            print(AddProduct())
        elif option == "2":
            print(SearchProduct())     
        elif option == "3":
            print(UpdatePrice())  
        elif option == "4":
            print(IncreaseStock())     
        elif option == "5":
            print(sellProduct())
        elif option =="6":
            print(Low_Stock(5))
        elif option == "7":
            print(Total_Inventory())
        elif option == "8":
            break
        else :
            print("enter valid option!")
ChooseOptions()