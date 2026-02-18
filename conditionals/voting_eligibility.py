# Program to check voting eligibility
"""WHAT: Checks whether a person is eligible to vote.
WHY: To verify age-based eligibility.
HOW: Uses if-else to compare age with minimum limit."""

age = int(input("Enter your age: "))

if age >= 18:
    print(age, "Congrats, you are eligible for voting")
else:
    print(age, "Sorry, you have to wait for", 18 - age, "years for voting")
