"""
Write a program that serves as a basic calculator.
It asks for two numbers, then it asks for an operator.
Gracefully deal with input that doesn't cleanly convert to numbers.
Deal with division by zero errors.
"""


# Function to add two numbers
def add(number1, number2):
    return number1 + number2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(number1, number2):
    return number1 * number2


# Function to divide two numbers
def divide(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return None


print("********Basic Calculator********")
input_number1 = int(input("Enter first number: "))
input_number2 = int(input("Enter second number: "))
print("Please select operation -\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")

# Take input from the user
select = input("Select operations form 1, 2, 3, 4 :")

if select == "1":
    print(input_number1, "+", input_number2, "=",
          add(input_number1, input_number2))

elif select == "2":
    print(input_number1, "-", input_number2, "=",
          subtract(input_number1, input_number2))

elif select == "3":
    print(input_number1, "*", input_number2, "=",
          multiply(input_number1, input_number2))

elif select == "4":
    print(input_number1, "/", input_number2, "=",
          divide(input_number1, input_number2))
else:
    print("Invalid input! Please select vaild operation and try again!!")
