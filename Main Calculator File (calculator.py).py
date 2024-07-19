# Importing functions from respective files
from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def calculator():
    while True:
        # Input two numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Input operator
        operator = input("Enter operator (+, -, *, /): ")

        # Perform operation based on operator
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator")
            continue

        # Display the result2
        print("Result:", result)

        # Ask to quit or continue
        choice = input("Do you want to quit the calculator? (Y/N): ")
        if choice.upper() == 'Y':
            break
        elif choice.upper() == 'N':
            continue
        else:
            print("Invalid choice. Continuing by default.")

if __name__ == "__main__":

    calculator()
