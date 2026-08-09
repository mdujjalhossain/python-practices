num = int(input('Enter your number: '))

# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i
# print(factorial)

factorial = 1
i = 1
while i <= num:
    factorial = factorial *i
    i += 1
print(factorial) 