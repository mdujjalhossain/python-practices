# [Expression for item in list]

# Example-1: Iteration with list comprehension
a = [10, 20, 30, 40, 50]
b = [i+5 for i in a]        # iteration: [expression, loop]
print(b)

c = []
for i in a:
    i = i+5
    c.append(i)
print(c)

# Example-2: Iteration through a string using list comprehension
# a = 'Hello World'
# b = [i for i in a]
# print(b)

# Example-3: Using range() function in list comprehension
# a = [i for i in range(1, 10, 2)]        # used expression to apply condition
# b = [i for i in range(2, 10, 2)]
# c = list(range(2, 10, 2))               # direct conversion, can't apply any condition
# print(a)        # output = [1,3,5,7,9]
# print(b)        # output = [2,4,6,8]
# print(c)        # output = [2,4,6,8]