
for row in range(6):
    for col in range(row+1):
        print(chr(65+row), end = ' ')
    print()
    
    
row = 0
while row <= 6:
    col = 0
    while col <= row + 1:
        print(chr(97+row), end =' ')
        col += 1
    print()
    row += 1