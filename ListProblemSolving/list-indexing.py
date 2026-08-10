a = [10, 20, 40, 60, 'phitron']

# print(a[-1])

# for i in range(len(a)):         # positive traversing
#     print(a[i])
    
for i in range(-1, -len(a)-1, -1):
    print(a[i])
    a[2] = 'tested'