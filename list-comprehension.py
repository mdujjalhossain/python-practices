# Taking multiple inputs from user and store it in a list


# problem-1: Taking multiple string input--------------
# a = input('Enter the string: ').split()
# print(a)

# problem-2: Taking multiple int input-----------------
# a = list( map(int, input('Enter the string: ').split()))     # map(ki korbo, karo upore apply kora hobe), 
# print(a)

# problem-3: Taking multiple float input---------------
a = list(map(float, input('Enter float: ').split()))
print(a)