Number1= int(input(" enter the first number: "))
Number2= int(input(" enter the second number: "))
Number3= int(input(" enter the third number: "))


if Number1 > Number2 and Number1>Number3:
    print(f"{Number1} is the largest!")
elif Number1 == Number2 and Number1>Number3:
     print(f"Two numbers are = {Number1} and the largest!")
elif Number1> Number2 and Number1==Number3:
    print(f"Two numbers are = {Number1} and the largest!")

elif Number2 >Number1 and Number2 > Number3:
    print(f"{Number2} is the largest!")
elif Number2> Number1 and Number2== Number3:
    print(f"Two numbers are = {Number2} and the largest!")
elif Number3 >Number1 and Number3 > Number2:
    print(f"{Number3} is the largest!")
else:
    print(f"All three numbers are equal!")
