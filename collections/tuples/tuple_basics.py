"""WHAT: Tuple is an ordered and immutable collection.
WHY: Used when data should not be changed.
HOW: Elements are stored in order and accessed using index."""

# Creating a tuple
numbers = (10, 20, 30, 40)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Length of tuple
print("Length of tuple:", len(numbers))

# Tuple can store mixed data types
mixed_tuple = (1, "Python", 3.5)
print("Mixed tuple:", mixed_tuple)
