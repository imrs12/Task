# 1 - Write a program to perform addition, subtraction, multiplication, and division of two numbers provided by the user.

# Taking Inputs from User 

num1= float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))

# Arithmetic Operations

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1/num2 if num2 != 0 else "Number cannot divide by zero"

# Results

print("\nResults: ")
print(f"Addition is {addition}")
print(f"Subtraction is {subtraction}")
print(f"Multiplication is {multiplication}")
print(f"Division is {division}")
