def is_prime(number):
    # that number is only divisible by itself and one
    
    if number<=1:
        return f"{number} is not prime."
    

    for i in range(2, int(number **0.5)+1):
        if number %i == 0:
            return f"{number} is not prime."
            
    return f"{number} is prime."

def get_divisors(number):
    lst=[]
    if number <0:
        return f"the number {number} has no positive divisors."
    if number>=1:
        for i in range(1,number+1):
            if number % i==0:
                lst.append(i)
    return f"the list of divisors: {lst}"       

def sum_of_digits(number):
    # first change the number to string to access every digits
    # and to calculate sum back it to integer
    number=abs(number)
    num=str(number)
    sum_of_digits=0
    for i in num:
      intI=int(i)
      sum_of_digits+=intI
    return f"sum of digits is: {sum_of_digits}"


def reverse_number(number):
    if number <0:
        number=abs(number)
        num=str(number)
        reversed=num[::-1]
        ReverseNumber= -int(reversed)
        return f"the reverse of number is: {ReverseNumber}"
    else:
        num=str(number)
        reversed=num[::-1]
        ReverseNumber=int(reversed)
    return f"the reverse of number is: {ReverseNumber}"


def even_or_odd(number):
    if number %2 ==0:
        return " it is Even!"
    else:
        return "it is Odd!"


def analyze_number(number):
    print(f"=======================\n          ANALYSIS \n=======================")
    IsPrime=is_prime(number)
    GetDivisors=get_divisors(number)
    SumDigits=sum_of_digits(number)
    ReverseNumber=reverse_number(number)
    EvenOdd=even_or_odd(number)


    print(IsPrime)
    print(GetDivisors)
    print(SumDigits)
    print(ReverseNumber)
    print(EvenOdd)
    print("=======================")


numb=int(input("Enter a number: "))
analyze_number(numb)   

        