import math
from colorama import Fore, Style

# Function to display the banner
def display_banner():
    banner = f"""
{Fore.GREEN}#################################################
#                                               #
#         Advanced Calculator with Colors       #
#                                               #
#################################################{Style.RESET_ALL}
"""
    print(banner)

# Function to perform basic math operations
def basic_operations(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        raise ValueError("Invalid operator!")

# Function to perform advanced math operations
def advanced_operations(operation, num):
    if operation == 'sqrt':
        return math.sqrt(num)
    elif operation == 'sin':
        return math.sin(math.radians(num))
    elif operation == 'cos':
        return math.cos(math.radians(num))
    elif operation == 'tan':
        return math.tan(math.radians(num))
    else:
        raise ValueError("Invalid operation!")

# Main calculator function
def calculator():
    display_banner()

    while True:
        try:
            print("Choose an operation:")
            print("1. Basic Math Operations (+, -, *, /)")
            print("2. Advanced Math Operations (sqrt, sin, cos, tan)")
            print("3. Exit")
            choice = int(input("Enter your choice (1/2/3): "))

            if choice == 1:
                num1 = float(input("Enter the first number: "))
                operator = input("Enter the operator (+, -, *, /): ")
                num2 = float(input("Enter the second number: "))

                result = basic_operations(num1, num2, operator)
                print("Result:", result)

            elif choice == 2:
                operation = input("Enter the operation (sqrt, sin, cos, tan): ")
                num = float(input("Enter the number: "))

                result = advanced_operations(operation, num)
                print("Result:", result)

            elif choice == 3:
                print("Exiting the calculator...")
                break

            else:
                print("Invalid choice! Please choose again.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()
  
