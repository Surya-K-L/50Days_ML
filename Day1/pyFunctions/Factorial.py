num=int(input("Enter a Number: "))
def Fact(num):
    fact=1
    for i in range(num,0,-1):
        fact=fact*i
    return fact

print(Fact(num))