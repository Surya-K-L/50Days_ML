#normal 
num=[]
for i in range(1,10):
    num.append(i)
print(num)
#list comprehension
a=[i for i in range(1,10)]
print(a)

#square of numbers
square=[i*i for i in range(1,10)]
print(square)

#with condition even numbers alone
even=[i for i in range(0,11) if i%2==0]
print(even)