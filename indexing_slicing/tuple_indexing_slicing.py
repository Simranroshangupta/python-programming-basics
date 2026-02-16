# TUPLE INDEXING AND SLICING
# Meaning:
# Tuples follow the same indexing and slicing rules as lists,
# but tuples are immutable (cannot be changed).

numbers = (10, 20, 30, 40, 50)

# Tuple indexing
print("Index 0:", numbers[0])
print("Index -1:", numbers[-1])

# Tuple slicing
print("Slice 1:4 ->", numbers[1:4])
print("Slice with step 2 ->", numbers[::2])
