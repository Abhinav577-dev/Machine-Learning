# creating the variables in the python 

#integer variables
a = 5
b = 6
print(type(a))
print(type(b))
print(a+b)

# String variable
c = "Hello python"
print(type(c))
print(c)

# float datatype
d = 9.76
print(type(d))

#type conversion
n = 30
m = float(n)
print(type(m))


#taking the input

num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))

print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")

op = input("which operation do you want to perform: ")

# conditional statements

if op == "Addition":
    print(f"the addition of {num1} and {num2} is : ", num1+num2)

elif op == "Subtraction":
    print(f"the subtraction of {num1} and {num2} is : ", num1-num2)

elif op == "Multiplication":
    print(f"the multiplication {num1} and {num2} is : ", num1*num2)

else:
    if num1 > num2:
        print(f"the division {num1} and {num2} is : ", num1/num2)
    else:
        print(f"the division {num1} and {num2} is : ", num2/num1)


# function in python

def add(a, b):
    return a+b

print(add(num1, num2))