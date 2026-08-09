# pop(), removes and returns the last value from the list or the given index------- 1
# a = [1,2,3,4,5]
# a.pop()
# print(a)        # output = [1,2,3,4]

# remove(), removes a given object from the list----------- 2
# a = [1,2,3,4,5]
# a.remove(4)
# print(a)        # output = [1,2,3,5]

# clear(), remove all the items from the list---------  3
# a = [1,2,3,4,5]
# a.clear()
# print(a)        # output = []

# reverse(), reverse objects of the list in a place----------   4
# a = [1,2,3,4,5]
# a.reverse()     
# print(a)          # output = [5,4,3,2,1]
# print(a[::-1])      # output = [5,4,3,2,1]

# sort(), sort a list in ascending or descending----------  5
a = [1,3,9,8,2,5,4]
a.sort()    # output = [1, 2, 3, 4, 5, 8, 9] sort ascending
a.sort(reverse = True)      # output = [9, 8, 5, 4, 3, 2, 1] sort descending
print(a)

# max(), calculates maximum of all the elements of the list---------    6
# a = [1,2,3,4,5,9]
# print(max(a))     # output = 9

# min(), calculates minimum of all the elements of the list---------    7
# a = [1,2,3,4,5,9]
# print(min(a))       # output = 1

