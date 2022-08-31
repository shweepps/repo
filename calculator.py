num1 = float(input("ENTER NUM 1 "))
OP = input("Enter operator ")
num2 = float(input("Enter num2 "))

if OP == "+":
    print(num1 + num2)
elif OP == "*":
    print(num1 * num2)
elif OP == "/":
    print(num1 / num2)
elif OP == "-":
    print(num1 - num2)
else:
    print("Invalid operator")

