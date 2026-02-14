# Dictionary Operations in Python

student = {
    "name": "Amit",
    "age": 20
}

print("Original dictionary:", student)

# Adding a new key-value pair
student["course"] = "AI & ML"
print("After adding course:", student)

# Updating a value
student["age"] = 21
print("After updating age:", student)

# Looping through dictionary
print("Student details:")
for key, value in student.items():
    print(key, ":", value)
