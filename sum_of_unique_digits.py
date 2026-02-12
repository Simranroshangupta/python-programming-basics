# Program to find the sum of unique digits of a number

ognum = int(input("Enter minimum 5-digit number: "))

num = ognum
digit = 0
rem = 0
sum = 0
mydigitlist = []   # null list

while num > 0:
    rem = num % 10
    digit = rem
    mydigitlist.append(digit)
    rem = 0
    num = int(num / 10)

uniqueList = []    # empty list

for x in mydigitlist:
    if x not in uniqueList:
        uniqueList.append(x)

if uniqueList:
    for y in uniqueList:
        sum = sum + y
    print("Sum of unique digits is", sum)
else:
    print("Please enter 5-digit number")
