# DEFAULT ARGUMENTS
# Meaning:
# Default arguments allow a function to use a default value
# if no argument is provided during the function call.

def greet(name="User"):
    print("Hello", name)

# Calling without argument (uses default value)
greet()

# Calling with argument (overrides default)
greet("Simran")
