Customer_name = input("Enter Customer name: ")
Product_name = input("Enter Product name: ")
Price = int(input("Enter the price: "))
Quantity=int(input("Enter Quantity: "))


Total_Price= Price * Quantity

print("========================================")
print("              RECEIPT")
print("========================================\n")

print(f"Customer: {Customer_name}\n\nProduct      Price       Quantity" )
print("----------------------------------------")
print(f"{Product_name}         {Price}ETB          {Quantity}\n\n")

print(f"Total: {Total_Price}ETB\n")

print("Thank you for shopping!") 
print("========================================")