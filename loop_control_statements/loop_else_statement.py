# Loop-Else Statement in Python

numbers = [2, 4, 6, 8]

for num in numbers:
    if num % 2 != 0:
        print("Odd number found")
        break
else:
    print("All numbers are even")
