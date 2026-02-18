#Keyword argument
"""WHAT: Arguments passed using parameter names.
WHY: To improve readability.
HOW: Values are matched by name."""
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

# Calling function using keyword arguments
student_info(age=20, name="Simran", course="Python")