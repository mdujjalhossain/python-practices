# Task: Write a program using conditional statement whether a number is even or odd, after taking number input from the user.

input = int(input('Enter the number: '))

if input % 2 == 0 :
    print(input, 'is even')
else:
    print(input, 'is odd')