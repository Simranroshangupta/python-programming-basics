# Program to find the sum of digits of a four-digit number

num = int(input("Enter your four-digit number: "))

rem = 0
add = 0

while num > 0:
    rem = num % 10
    add = add + rem
    num = int(num / 10)

print("Sum of its digits is,", add)
