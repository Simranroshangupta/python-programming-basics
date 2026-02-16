# KEYWORD ARGUMENTS
# Meaning:
# Keyword arguments allow us to pass values by parameter name,
# not by position. This improves clarity and avoids confusion.

# Defining a function
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

# Calling function using keyword arguments
student_info(age=20, name="Simran")
