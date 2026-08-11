# string problem solving: string sorting---------------
# input : x3b4U5i2
# output: bbbbiiUUUUUxxx

# a = input('Enter the value: ')
# res = ''
# for i in range(0, len(a), 2):
#     # res = res + a[i]
#     # print(f"{a[i]} {a[i+1]}")
#     res = res + a[i] * int(a[i+1])
# result = sorted(res, key = str.casefold)
# print(''.join(result))


# Palindrome string checking --------------

# a = input('Enter string: ')
# if a == a[::-1]:
#     print('Yes this is palindrome')
# else:
#     print('No! This is not a palindrome string')
    
    
# string reversing ----------------
# input: 'I love coding using Python'
# output: 'I evol gnioc gnisc nohtyP'

a = input('Enter the string: ')
a = a.split(' ')
result = ''
for i in a:
    result += i[::-1] + ' '
print(result)





