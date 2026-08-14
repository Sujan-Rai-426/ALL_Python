num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter any operator symbol [+, -, *, %, /, //, **, avg ] : ")

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
modules = num1 % num2
division = num1 / num2
floor_division = num1 // num2
power = num1 ** num2
average = (num1+num2) / 2

if operator == "+":
    print(num1, " + ", num2, " = ", addition)
elif operator == "-":
    print(num1, " - ", num2, " = ", subtraction)
elif operator == "*":
    print(num1, " * ", num2, " = ", multiplication)
elif operator == "%":
    print("Modules of ", num1, "&", num2, " = ", modules)
elif operator == "/":
    print(num1, " / ", num2, " = ", division)
elif operator == "//":
    print("Floor or Integer Division of ", num1, "&", num2," is ", floor_division)
elif operator == "**":
    print(num1, "^", num2, " = ", power)
elif operator == "avg":
    print("Average of ", num1, "&", num2, " is ", average)
else:
    print("Invalid OPERATOR input ")

