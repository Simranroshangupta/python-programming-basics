# GLOBAL VARIABLES
# Meaning:
# A global variable is defined outside all functions.
# It can be accessed inside functions, but not modified directly.

count = 10  # Global variable

def display_count():
    print("Count inside function:", count)

# Calling function
display_count()

# Accessing global variable outside function
print("Count outside function:", count)
