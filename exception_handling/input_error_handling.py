# Input Error Handling in Python
"""WHAT: Handles invalid input errors.
WHY: To ensure correct input from user.
HOW: Uses try-except to catch ValueError."""

while True:
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
        break

    except ValueError:
        print("Invalid input! Please enter a number.")
