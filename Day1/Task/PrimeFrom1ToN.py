num=int(input("Enter a Number: "))

def Prime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

for i in range(1,num+1):
    if Prime(i):
        print(i,end=" ")