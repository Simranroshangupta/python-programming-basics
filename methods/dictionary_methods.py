# DICTIONARY METHODS
# Meaning:
# Dictionaries store data in key–value pairs.
# Dictionary methods are used to access, add, remove,
# and manipulate this data.

student = {
    "name": "Simran",
    "age": 20,
    "course": "Python"
}

# Access value using key
print("Name:", student.get("name"))

# Get all keys
print("Keys:", student.keys())

# Get all values
print("Values:", student.values())

# Get all key-value pairs
print("Items:", student.items())

# Add a new key-value pair
student.update({"grade": "A"})
print("After update:", student)

# Remove a key-value pair
student.pop("age")
print("After pop:", student)
