# LOCAL VARIABLES
# Meaning:
# A local variable is defined inside a function.
# It can be accessed only within that function.

def show_message():
    message = "Hello from local variable"
    print(message)

# Calling the function
show_message()

# The line below would cause an error if uncommented
# print(message)  # NameError: message is not defined
