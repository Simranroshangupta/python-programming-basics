# Input Error Handling in Python

while True:
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
        break

    except ValueError:
        print("Invalid input! Please enter a number.")
