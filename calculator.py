import sys

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select option: What operation would you like to perform.")
print("(1) Addition")
print("(2) Subtraction")
print("(3) Multiplication")
print("(4) Division")


while True:
    choice = input("Select your choice(1/2/3/4): ")
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Put your first number: "))
            num2 = float(input("Put your second number: "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    

        additional_calculation = input("Do you want to do next calculation? (yes/no): ")
        if additional_calculation == "no":
            sys.exit("Have a nice day!")   
    else:
        print("Invalid input")