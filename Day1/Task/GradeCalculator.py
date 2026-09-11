mark=int(input("Enter your mark: "))
if(mark>=90 and mark<=100):
    print("A+")
elif(mark>=80 and mark<=89):
    print("A")
elif(mark>=70 and mark<=79):
    print("B")
elif(mark>=60 and mark<=69):
    print("C")
elif(mark>=50 and mark<=59):
    print("D")
elif(mark<50 and mark>=0):
    print("Fail")
else:
    print("Not a Valid Mark")