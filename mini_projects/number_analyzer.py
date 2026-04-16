# ==============================
# Number Analyzer Project
# ==============================

# This program analyzes a number and tells:
# - Even or Odd
# - Prime or Not Prime
# - Palindrome or Not
# - Factorial of the number


# ------------------------------
# Function to check even/odd
# ------------------------------
def is_even(n):
    """
    Returns True if number is even, else False
    """
    return n % 2 == 0


# ------------------------------
# Function to check prime
# ------------------------------
def is_prime(n):
    """
    Returns True if number is prime, else False
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# ------------------------------
# Function to check palindrome
# ------------------------------
def is_palindrome(n):
    """
    Returns True if number is palindrome
    Example: 121 → True
    """
    return str(n) == str(n)[::-1]


# ------------------------------
# Function to calculate factorial
# ------------------------------
def factorial(n):
    """
    Returns factorial of a number
    If negative, returns None
    """
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


# ------------------------------
# Main function (entry point)
# ------------------------------
def main():
    print("================================")
    print("        Number Analyzer         ")
    print("================================")

    try:
        # Taking input from user
        num = int(input("Enter a number: "))

        print("\n----- Results -----")

        # Even or Odd
        if is_even(num):
            print("Even Number")
        else:
            print("Odd Number")

        # Prime check
        if is_prime(num):
            print("Prime Number")
        else:
            print("Not a Prime Number")

        # Palindrome check
        if is_palindrome(num):
            print("Palindrome Number")
        else:
            print("Not a Palindrome")

        # Factorial
        fact = factorial(num)
        if fact is not None:
            print("Factorial:", fact)
        else:
            print("Factorial not defined for negative numbers")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


# ------------------------------
# Program starts here
# ------------------------------
if __name__ == "__main__":
    main()