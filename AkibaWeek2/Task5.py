number = int(input("enter a number: "))

sum = 0
while number > 0:
    m= int(number % 10)     # use %10 to get the last digit
    sum= m + sum
    number = number// 10         # use //10 to eliminate or chop off the last digit 
                        # so until the last digit is gonna reach zero, or left nothing 
print(sum)              # it adds up the digits to the previous sum