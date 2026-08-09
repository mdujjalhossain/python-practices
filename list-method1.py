# list build in method for marge or sum items ---------------   1
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)        #output = [1,2,3,4,5,6]

# list(), converts string to list---------------    2
# s = 'Hello!'
# print(list(s))      # output = ['H', 'e', 'l', 'l', 'o', '!']

# append(), adds an element at end of the list---------------   3
# a = [12, 24, 36]
# a.append(48)
# print(a)        # output = [12, 24, 36, 48]

# insert(), adds an element at the specified position---------------    4
# a = [12, 36, 48]
# a.insert(1, 24)
# print(a)          # output = [12, 24, 36, 48]

# copy(), returns a copy of the list-------------    5
# a = [12, 36, 48]
# b = a.copy()
# b = a
# print(b)          # output = [12, 36, 48]

# count(), returns the number of elements with the specified value-------------   6
# a = [1,2,3,2,3,3,4,5,2,5,5,1]
# print(a.count(5))           # output = 3

# extend(), add the elements of a list to the end of the current list------------   7
a = [12, 23, 34]
# a.extend([80, 90])
a = a + [80, 90]
print(a)        # output = [12, 23, 34, 80, 90]











