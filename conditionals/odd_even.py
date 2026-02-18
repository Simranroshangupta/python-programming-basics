"""WHAT: Checks whether a number is odd or even.
WHY: To classify numbers based on divisibility by 2.
HOW: Uses modulus operator (%) with if-else."""

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number") 
