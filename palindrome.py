# Program to check whether a number is palindrome or not

ognum = int(input("Enter your number: "))

x = ognum
revnum = 0
rem = 0

while ognum > 0:
    rem = ognum % 10
    revnum = (revnum * 10) + rem
    ognum = int(ognum / 10)

if x == revnum:
    print(x, "is a Palindrome number")
else:
    print(x, "is Not a Palindrome number")
