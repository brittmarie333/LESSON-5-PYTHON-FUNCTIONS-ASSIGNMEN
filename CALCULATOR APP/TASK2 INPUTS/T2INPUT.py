#Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

print("enter an option for an answer")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
option = input()  

if option == "1":
        num1 = int(input("first number: "))
        num2 = int(input("second number: "))
        print(f"The sum is: {add(num1, num2)}")
elif option == "2":
        num1 = int(input("first number: "))
        num2 = int(input("second number: ")) 
        print(f"The difference is: {subtract(num1, num2)}")
elif option == "3":
        num1 = int(input("first number: "))
        num2 = int(input("second number: "))
        print(f"The product is: {multiply(num1, num2)}")
elif option == "4":
        num1 = int(input("first number: "))
        num2 = int(input("second number: "))
        print(f"The result is: {divide(num1, num2)}")
else:
        print("ERROR: Invalid option")
