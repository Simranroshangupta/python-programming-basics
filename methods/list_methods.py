# LIST METHODS
# Meaning:
# List methods are built-in operations used to add, remove,
# and modify elements in a list.
# Lists are mutable, so methods can change the original list.

numbers = [10, 20, 30]

# Adds an element at the end of the list
numbers.append(40)
print("After append:", numbers)

# Inserts an element at a specific position
numbers.insert(1, 15)
print("After insert:", numbers)

# Removes a specific element
numbers.remove(20)
print("After remove:", numbers)

# Removes and returns the last element
last_item = numbers.pop()
print("Popped item:", last_item)
print("After pop:", numbers)

# Sorts the list in ascending order
numbers.sort()
print("After sort:", numbers)
