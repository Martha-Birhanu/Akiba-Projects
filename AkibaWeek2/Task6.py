Start_num=int(input(" Enter a start number : "))
End_num = int(input(" Enter end number: "))


for i in range(Start_num,End_num + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)