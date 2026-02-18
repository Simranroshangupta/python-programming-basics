# Program to check prime number using count method
"""WHAT: Checks whether a number is prime.
WHY: To identify numbers divisible only by 1 and itself.
HOW: Counts number of divisors using a loop."""

num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is Not a Prime number")
