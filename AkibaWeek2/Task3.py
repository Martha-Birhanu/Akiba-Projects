number= int(input("Enter number: "))


if number<=1:
    print("it is not prime!")
else:
    is_prime = True             # assumption 

for num in range(2,int(number**0.5) + 1):   # checking the numbers divisibility up to its square root.
    if number % num == 0:                   # the reason why we only do check the divisibilty upto its 
        is_prime = False                    # square root is that after the square root there are repeated pairs.                                   
        break     # if we got one divider which proves that the number is not prime, the program breaks, because it is enough to prove the assumption is wrong.

if is_prime:
    print("it is a prime!")
else:
    print("it is not prime!")



