# USER-DEFINED FUNCTIONS
"""WHAT: Functions created by the programmer.
WHY: To perform specific tasks.
HOW: Defined using def with parameters and return."""


def greet(name):
    print("Hello", name)

def add(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0


# Calling user-defined functions
greet("Simran")
greet("Python")

result = add(10, 20)
print("Sum:", result)

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))
