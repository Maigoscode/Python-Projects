# Simple Calculator:
# Build a basic calculator that can perform basic-
# arithmetic operations like addition, subtraction, multiplication,
# and division.

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# addition

if op == "+":
  print(num1 + num2)

  # subtraction

elif op == "-":
  print(num1 - num2)

  # multiplication

elif op == "*":
  print(num1 * num2)

  # division

elif op == "/":
  print(num1 / num2)
else:
  print("Invalid operator")