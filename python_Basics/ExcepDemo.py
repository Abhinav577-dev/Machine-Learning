# Handling the exceptions using the try, except, else, finally

try:
    x = int(input("Enter the no: "))
    ans = 34/x
    

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print(f"Invalid input")

else:
    print(f"ans is {ans}")

finally:
    print("end of program")