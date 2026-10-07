
Secret_number= 6
is_correct=False
number_of_attempts=0
print("You only have 5 attempts!")
for i in range(5):
    User_guess= int(input("enter Your Guess: "))
    number_of_attempts+=1
    if User_guess == Secret_number:
        is_correct = True
        break
    
if is_correct:
    print("Congratulations!")
    print(f"you guessed the number in {number_of_attempts} attempts.")
else:
    print(" Game over!")

    