# STRING SLICING
# Meaning:
# Slicing is used to extract a part (substring) from a string.
# Syntax: string[start : end : step]

text = "PYTHONPROGRAM"

# Slice from index 0 to 5 (end index not included)
print("Slice 0:6 ->", text[0:6])

# Slice from index 6 to end
print("Slice 6:end ->", text[6:])

# Slice from beginning to index 6
print("Slice start:6 ->", text[:6])

# Slice using step value
print("Slice with step 2 ->", text[::2])

# Reverse the string using slicing
print("Reverse string ->", text[::-1])
