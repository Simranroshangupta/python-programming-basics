# List Operations in Python

fruits = ["apple", "banana", "mango"]

print("Original list:", fruits)

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Inserting element at specific position
fruits.insert(1, "grapes")
print("After insert:", fruits)

# Removing element
fruits.remove("banana")
print("After remove:", fruits)

# Popping last element
removed_item = fruits.pop()
print("Removed item:", removed_item)
print("After pop:", fruits)

# Checking length of list
print("Total elements in list:", len(fruits))
