Balance= 1000
PIN=1234
number_of_attempts=3
is_Correct=False

for i in range(3):
    User_PIN=int(input("Enter your pin: "))
    number_of_attempts -=1
    if User_PIN==PIN:
        is_Correct=True
        print(" Welcome to AKIBA Bank! ")
        while True:
            print(f"==== AKIBA BANK ==== \n1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit")
            option=input(" Choose an option: ")

            if option == "4":
                break

            elif option == "1":
                print(f"Your Current Balance is: {Balance} ETB")
            elif option == "2":
                depost=int(input("Enter the Amount to deposit: "))
                Balance+=depost
                print(f"Deposit successful! \nYour current Balance is:{Balance}")
            elif option == "3":
                withdraw=int(input("Enter the Amount to Withdraw: "))
                if withdraw < Balance:
                    Balance -= withdraw 
                    print(f"Withdraw Successful! \nYour current Balance is: {Balance} ")
                else:
                    print("Insufficient balance!") 

            else:
                print(f"Invalid option.\nPlease choose a valid option. ")
        break
    print(f"Incorrect PIN. \nAttempts remaining: {(number_of_attempts)}")   
    
if not is_Correct:
    print(f"Too many incorrect attempts.\nYour account has been locked.")



    


























# while True:
#     print(f"==== AKIBA BANK ==== \n1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit")
#     option=input(" Choose an option: ")

#     if option == "4":
#         break

#     elif option == "1":
#         print(f"Your Current Balance is: {Balance} ETB")
#     elif option == "2":
#         depost=int(input("Enter the Amout to deposit: "))
#         Balance+=depost
#         print(f"Deposit successful! \nYour current Balance is:{Balance}")
#     elif option == "3":
#         withdraw=int(input("Enter the Amount to Withdraw: "))
#         if withdraw < Balance:
#             Balance -= withdraw 
#             print(f"Withdraw Successful! \nYour current Balance is: {Balance} ")
#         else:
#             print("Insufficient balance!") 

#     else:
#         print(f"Invalid option.\nPlease choose a valid option. ")