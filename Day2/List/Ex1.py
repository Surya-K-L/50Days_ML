num=[10,20,30,40,50]
"""Print the first element
Print the last element
Change 30 to 100
Add 60
Remove 20
Print the length
Print every number using a loop"""

print(num[0])
print(num[len(num)-1])
num[2]=100
print(num)
num.append(60)
print(num)
num.remove(20)
print(num)
print(len(num))

for n in num:
    print(n,end=" ")