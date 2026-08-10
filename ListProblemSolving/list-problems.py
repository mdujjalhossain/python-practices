# problem -1: swapping between two list element----------
# a = [12,14,12,23,19]
# temp = a[0]
# a[0] = a[-1]
# a[-1] = temp
# print(a)      # output: [19,14,1,23,12]

#problem- 2: Count the unique elements in the list------------
# a = [1,2,2,3,4,5,6,6]
# b = []
# count = 0
# for i in a:
#     if i not in b:
#         count = count+1
#         b.append(i)
# print(count)      # output: 6
 
# problem- 3: given a list, extract all elements whose frequency is greater then K.----------------
# input: test_list = [4,6,4,3,3,4,3,4,3,8], K = 3
# output: [4,3]

# test_list = [4,6,4,3,3,4,3,4,3,8]
# K = 3
# res =[]

# for i in test_list:
#     freq = test_list.count(i)
#     if freq > 3 and i not in res:
#         res.append(i)
# print(res)


# problem -4 : create the following list using list comprehension -----------------
# [[1,2,3,4], [0,2,3,4], [0,1,2,4], [0,1,2,3]]

a = [[j for j in range(5) if i!=j] for i in range(5)]
print(a)

b = []
for i in range(5):
    c = []
    for j in range(5):
        if i != j:
            c.append(j)
    b.append(c)
print(b)






