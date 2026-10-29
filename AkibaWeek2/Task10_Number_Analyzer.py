
lst=[]
num_of_evens=0
num_of_odds=0
total_sum=0
for i in range(1,11):
    num=int(input(f"Enter number {i}: "))
    lst.append(num)
    total_sum += num
    if num % 2==0:
        num_of_evens += 1
    else:
        num_of_odds += 1

largest_number=max(lst)
smallest_number=min(lst)
average = total_sum/len(lst)

print(f"Largest Number = {largest_number} \nSmallest Number = {smallest_number} \nTotal Sum = {total_sum} \nAverage = {average} \nTotal number of even numbers = {num_of_evens} \nTotal number of odd numbers = {num_of_odds}")






        


