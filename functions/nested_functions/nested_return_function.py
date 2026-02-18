# NESTED FUNCTION WITH RETURN
# Meaning:
# A function can define another function inside it
# and return that inner function.
# This helps in data hiding and structured logic.

def outer_function():
    message = "Hello from inner function"

    def inner_function():
        return message

    # Returning the inner function
    return inner_function

# Calling outer function
result_function = outer_function()

# Calling returned inner function
print(result_function())
