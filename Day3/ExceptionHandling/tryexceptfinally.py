try:
    a=int(input("Enter a Number: "))
    b=int(input("Enter a Number: "))
    print(a/b)
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("Program completed")