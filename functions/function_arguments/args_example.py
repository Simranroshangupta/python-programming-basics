# *args (VARIABLE NUMBER OF POSITIONAL ARGUMENTS)
# Meaning:
# *args allows a function to accept any number of positional arguments.
# Internally, arguments are stored as a tuple.

def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Calling function with different number of arguments
print("Sum of 2 numbers:", add_numbers(10, 20))
print("Sum of 4 numbers:", add_numbers(1, 2, 3, 4))
print("Sum of many numbers:", add_numbers(5, 10, 15, 20, 25))
