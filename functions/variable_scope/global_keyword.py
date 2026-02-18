# GLOBAL KEYWORD
# Meaning:
# The global keyword is used when we want to modify
# a global variable inside a function.

count = 0  # Global variable

def increment():
    global count
    count += 1
    print("Count inside function:", count)

# Calling function multiple times
increment()
increment()
increment()

print("Count outside function:", count)
