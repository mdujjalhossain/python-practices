# Task: Take three integer inputs from the user and find the largest number using if-elif-else statement.

num1 = int(input('1st number: '))
num2 = int(input('2nd number: '))
num3 = int(input('3rd number: '))

if num1 >= num2 and num1 >= num3:
    print('The largest number is:', num1)
elif num2 >= num1 and num2 >= num3:
    print('The largest number is:', num2)
else:
    print('The largest number is:', num3)