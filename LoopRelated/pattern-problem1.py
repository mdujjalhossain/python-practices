
# for row in range(5):
#     for col in range(col+1):
#         print('#', end =' ')
#     print()


row = 0
while row <= 3:       
    col = 0
    while col <= row: 
        print('#', end=' ')
        col += 1
    print()
    row += 1

    