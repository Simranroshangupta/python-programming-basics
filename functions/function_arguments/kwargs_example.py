# **kwargs (VARIABLE NUMBER OF KEYWORD ARGUMENTS)
# Meaning:
# **kwargs allows a function to accept any number of keyword arguments.
# Internally, arguments are stored as a dictionary.

def student_details(**details):
    for key, value in details.items():
        print(key, ":", value)

# Calling function with keyword arguments
student_details(name="Simran", age=20, course="Python")
