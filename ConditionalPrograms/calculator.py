x = int(input("Enter the first variable :"))
y = int(input("Enter the second variable :"))

operation = int(input("Please select an operation to be performed \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n >"))

if operation == 1:
    print("Addition = " + str(x + y))
elif operation == 2:
    print("Subtraction = " + str(x - y))
elif operation == 3:
    print("Multiplication = " + str(x * y))
elif operation == 4:
    print("Division = " + str(x / y))