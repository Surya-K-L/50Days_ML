a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
op=input("Enter the Operator: ")
if(op=="+"):
    print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    if(b!=0):
        print(a/b)
    else:
        print("Cannot divide by zero")
elif(op=='%'):
    if(b!=0):
        print(a%b)
    else:
        print("Cannot calculate remainder by zero")
elif(op=='**'):
    print(a**b)
elif(op=='//'):
    if(b!=0):
        print(a//b)
    else:
        print("Cannot perform floor division by zero")
else:
    print("Invalid Operator")
    