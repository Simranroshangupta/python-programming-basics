# Program to demonstrate if-else statement with nested decisions

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")

    if age >= 60:
        print("You belong to the Senior Citizen category.")
    else:
        print("You belong to the Adult category.")
else:
    print("You are not eligible to vote.")
    print("You belong to the Minor category.")
