print("Python Calculator")
print("Enter one of the operators for calculations")

print("For addition enter '+' Symbol")
print("For addition enter '-' Symbol")
print("For addition enter '*' Symbol")
print("For addition enter '/' Symbol")

operator = input("Enter the operator: ")
num1 = float(input("Enter the first Number: "))
num2 = float(input("Enter the second Number: "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Entry")