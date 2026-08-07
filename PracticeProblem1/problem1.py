# Task: Take the values of length and width of a rectangle from the user and check if it is a square or not.

length = int(input('Enter the length: '))
width = int(input('Enter the width: '))

if length == width:
    print('This is a square')
else:
    print('This is not a square')

# print(type(length))