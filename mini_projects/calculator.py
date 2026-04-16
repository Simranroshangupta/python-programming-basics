# =====================================
# Advanced Menu-Based Calculator
# =====================================

import math

# ------------------------------
# Operation functions
# ------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


def square_root(a):
    if a < 0:
        return "Error: Negative number"
    return math.sqrt(a)


# ------------------------------
# Display menu
# ------------------------------

def show_menu():
    print("\n========= Calculator =========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Modulus (%)")
    print("7. Square Root (√)")
    print("8. View History")
    print("9. Exit")


# ------------------------------
# Main program
# ------------------------------

def main():
    history = []   # stores previous calculations

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '9':
            print("Exiting Calculator...")
            break

        # View history
        if choice == '8':
            print("\n--- Calculation History ---")
            if not history:
                print("No history available.")
            else:
                for item in history:
                    print(item)
            continue

        try:
            # Square root (single input)
            if choice == '7':
                num = float(input("Enter number: "))
                result = square_root(num)
                print("Result:", result)
                history.append(f"√{num} = {result}")
                continue

            # Other operations (two inputs)
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = "+"

            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"

            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"

            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"

            elif choice == '5':
                result = power(num1, num2)
                operation = "^"

            elif choice == '6':
                result = modulus(num1, num2)
                operation = "%"

            else:
                print("Invalid choice! Please select from 1-9.")
                continue

            print("Result:", result)

            # Save result in history
            history.append(f"{num1} {operation} {num2} = {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")


# ------------------------------
# Entry point
# ------------------------------

if __name__ == "__main__":
    main()