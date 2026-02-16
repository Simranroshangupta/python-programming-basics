# DEFAULT ARGUMENTS
# Meaning:
# Default arguments allow a function to use a default value
# if no value is provided while calling the function.

# Defining a function with a default parameter
def greet(name="User"):
    print("Hello", name)

# Calling the function without argument
greet()

# Calling the function with argument
greet("Alice")
