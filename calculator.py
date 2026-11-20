
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

num1=int(input("enter a number:"))
num2 =int(input("enter a number:"))
operator=input("choose opertation :")
if operator== "+":
    print(f"{num1}+{num2}={add(num1,num2)}")
elif operator=="-":
    print(f"{num1}-{num2}={subtract(num1,num2)}")
elif operator=="/":
    print(f"{num1}/{num2}={divide(num1,num2)}")
elif operator=="*":
   print(f"{num1}*{num2}={multiply(num1,num2)}")