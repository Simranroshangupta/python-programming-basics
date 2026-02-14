# List Programs in Python

# Program 1: Sum of elements in a list
numbers = [10, 20, 30, 40]

total = 0
for num in numbers:
    total = total + num

print("Sum of list elements:", total)


# Program 2: Find the largest element in a list
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element in the list:", largest)
