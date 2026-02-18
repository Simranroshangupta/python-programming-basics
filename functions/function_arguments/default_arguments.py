# DEFAULT ARGUMENTS
"""WHAT: Function that accepts input values.
WHY: To work with different data.
HOW: Values are passed as arguments."""


def greet(name="User"):
    print("Hello", name)

# Calling without argument (uses default value)
greet()

# Calling with argument (overrides default)
greet("Simran")
