# RECURSIVE FUNCTIONS
# Meaning:
# A recursive function is a function that calls itself
# to solve a problem in smaller steps.
# Every recursive function must have a base condition.

def factorial(n):
    # Base condition: stops recursion
    if n == 1:
        return 1
    # Recursive call
    return n * factorial(n - 1)

# Calling recursive function
print("Factorial of 5:", factorial(5))
