
a = int(input('Enter the number: '))

count = 0
while a > 0:
    a = a // 10
    count = count + 1
print(count)


# method-2 ------------
# input = input('Enter the number: ')
# print(len(input))             # len(), function count the length of string data
