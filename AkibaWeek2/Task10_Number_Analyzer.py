
lst=[]
num_of_evens=0
num_of_odds=0
total_sum=0
for i in range(0,10):
    num=int(input("Enter number: "))
    lst.append(num)
    total_sum += num
    if num % 2==0:
        num_of_evens += 1
    else:
        num_of_odds += 1

largest_number=max(lst)
smallest_number=min(lst)
Average = total_sum/len(lst)

print(largest_number)
print(smallest_number)
print(total_sum)
print(Average)
print(num_of_evens)
print(num_of_odds)






        


