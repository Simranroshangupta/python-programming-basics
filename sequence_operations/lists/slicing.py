# LIST SLICING
# Meaning:
# Slicing is used to extract a portion of a list.
# Syntax: list[start : end : step]

numbers = [10, 20, 30, 40, 50, 60]

# Slice from index 1 to 4 (end index not included)
print("Slice 1:4 ->", numbers[1:4])

# Slice from beginning to index 3
print("Slice start:3 ->", numbers[:3])

# Slice from index 3 to end
print("Slice 3:end ->", numbers[3:])

# Slice with step value
print("Slice with step 2 ->", numbers[::2])

# Reverse the list using slicing
print("Reverse list ->", numbers[::-1])
