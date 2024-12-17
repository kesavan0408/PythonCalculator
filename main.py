num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("choose the operation(+,-,*,/,^): ")
if operation == '+' :
    result = num1 + num2
    print(result)
elif operation == '-' :
    result = num1 - num2
    print(result)
elif operation == '*' :
    result = num1 * num2
    print(result)
elif operation == '/' :
    result = num1 / num2
    print(result)
elif operation == '^' :
    result = num1 ^ num2
    print(result)
else:
    print("invalid input")
    print (f"The result is{result}")
