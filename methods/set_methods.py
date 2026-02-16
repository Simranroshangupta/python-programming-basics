# SET METHODS
# Meaning:
# Sets store unique elements.
# They are unordered and do not allow duplicates.
# Set methods are used for mathematical set operations.

numbers = {10, 20, 30}

# Adds an element to the set
numbers.add(40)
print("After add:", numbers)

# Removes an element
numbers.remove(20)
print("After remove:", numbers)

# Another set for operations
more_numbers = {30, 40, 50}

# Union of sets (all unique elements)
print("Union:", numbers.union(more_numbers))

# Intersection of sets (common elements)
print("Intersection:", numbers.intersection(more_numbers))

# Difference of sets
print("Difference:", numbers.difference(more_numbers))
