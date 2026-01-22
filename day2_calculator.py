a = float(input("first number: "))
b = float(input("second number: "))
op = input("Choose operation(+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Unknown operation:", op)          