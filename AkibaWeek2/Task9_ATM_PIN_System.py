

pin=1234

number_of_attempts=3
is_correct=False

for i in range(3):
    User_Pin = int(input(" Enter Your PIN: "))
    number_of_attempts -=1
    if User_Pin == pin:
        is_correct=True
        print("Access Granted!")
        break
    print(f"Incorrect PIN. \nAttempts remaining: {(number_of_attempts)}")

if not is_correct:
    print("Access denied!")   
    
