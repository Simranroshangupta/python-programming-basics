# Basic Try-Except in Python
"""WHAT: Handles runtime errors using try and except.
WHY: To prevent program crash.
HOW: Executes risky code in try and handles errors in except."""

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input! Please enter a number.")
