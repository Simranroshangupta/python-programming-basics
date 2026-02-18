# Try-Except-Finally in Python
"""WHAT: Handles errors and executes final code.
WHY: To ensure cleanup code always runs.
HOW: finally block executes regardless of error."""

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program execution completed.")
