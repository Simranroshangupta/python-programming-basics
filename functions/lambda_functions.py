# LAMBDA FUNCTIONS
# Meaning:
# Lambda functions are small anonymous functions written in one line.
# They are used when a simple function is needed for a short time.

# Lambda function for addition
add = lambda a, b: a + b
print("Sum:", add(5, 3))

# Lambda function for square
square = lambda x: x * x
print("Square of 4:", square(4))

# Lambda function used with built-in function
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)
