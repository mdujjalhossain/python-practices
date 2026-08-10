# 2D list comprehension
# Transpose matrix e conversion
matrix = [[1,2], [3,4], [5,6], [7,8]]

a = []
for row in range(2):
    b = []
    for col in matrix:
        b.append(col[row])
    a.append(b)
print('a: ' ,a)

b = [[col[row] for col in matrix] for row in range(2)]
#   --- i ---  --- inner-loop---   ---- outer-loop----
print('b: ' ,b)



    