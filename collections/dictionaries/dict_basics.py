#Dictionary in python
"""WHAT: Dictionary stores data in key–value pairs.
WHY: Used to represent structured data.
HOW: Values are accessed using unique keys."""

# Creating a dictionary
student = {
    "name": "Amit",
    "age": 20,
    "course": "AI & ML"
}

# Printing the dictionary
print("Student details:", student)

# Accessing values using keys
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])

# Length of dictionary
print("Total number of keys:", len(student))
