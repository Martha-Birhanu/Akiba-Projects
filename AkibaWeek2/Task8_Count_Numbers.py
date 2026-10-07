N = int(input("Enter a positive number: "))


Even=0
Odd=0
Total_All =0
for n in range(1,N +1):
    Total_All += n
    if n % 2 == 0:
        Even= Even+1
    else:
        Odd = Odd + 1
print(f"{Even} numbers are Even.")
print(f"{Odd} numbers are odd.")

print(f"The Sum of all numbers = {Total_All}")
