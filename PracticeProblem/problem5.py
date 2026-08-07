# Write a program to check whether a year is leap year or not. take input from user:
# if year= 1996, it is leap year.

# Conditions for leap year:
# 1. If a year is divisible by both 400 and 100, it is leap year.
# 2. If a year is divisible by 4 and not divisible by 100, it is leap year.

year = int(input('Enter the year: '))

# method - 1------------
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, 'is leap year')
# else:
#     print(year, 'is not leap year')
    
# method -2 -------------
if (year % 4 == 0) and (year % 100 != 0):
    print(year, 'is leap year')
elif (year % 400 == 0) and (year % 100 == 0):
    print(year, 'is leap year')
else:
    print(year, 'is not leap year')
