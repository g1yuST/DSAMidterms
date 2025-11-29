# First: ask for numbers
try:
    choice = input("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square\n6. Modulo\nEnter choice (1/2/3/4/5/6): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Syntax Error!")
    exit()

# Function to add two numbers
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def square(n1, n2):
    return n1 ** n2

def modulo(n1, n2):
    return n1 % n2


# Perform calculation
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
elif choice == '5':
    print("Result:", square(num1, num2))
elif choice == '6':
    print("Result:", modulo(num1, num2))
else:
    print("Syntax Error!")
