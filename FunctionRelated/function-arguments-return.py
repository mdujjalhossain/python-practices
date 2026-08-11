# Function with no argument and no return value in Python-----------
# def greeting():
#     print('Hello! Good Morning.')
# greeting()

# def sum():
#     a = int(input('Enter first number: '))
#     b = int(input('Enter second number: '))
#     print( 'sum is: ',a+b)
# sum()


# Function with no argument but return value in Python-----------
# def add():
#     a = 4
#     b = 5
#     return a + b
# result = add()
# print(result + 11)


# Function with argument but no return value in Python
# def add(a=10,b=5):
#     result = (a + b)+10
#     print(result)
# add()
# add(4,7)


# Function with argument and return value in Python
def juice_maker(a,b):
    res = f'mixture of {a} and {b} juice is ready!'
    return res
result = juice_maker('apple', 'orange')
result2 = juice_maker('banana', 'mango')
print(result)
print(result2)




