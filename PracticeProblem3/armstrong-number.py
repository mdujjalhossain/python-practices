# num = int(input('Enter the number: '))
# num_length = len(str(num))
# temp = num
# sum = 0

# while temp > 0:
#     last_num = temp % 10 
#     sum = sum + last_num ** num_length
#     temp = temp//10
# if sum == num:
#     print('This is an armstrong number')
# else:
#     print('This is not a armstrong number')


# method - 02   -----------------
num = input()
num_length = len(num)
sum = 0

for i in num:
    sum = sum + int(i)** num_length
if int(num) == sum:
    print('This is an armstrong number')
else:
    print('This is not a armstrong number')
    