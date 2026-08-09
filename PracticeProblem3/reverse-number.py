# num = int(input('Enter the number: '))
# temp = num          # to protect the real number
# reverse_a = 0

# while temp > 0:
#     last_digit = temp % 10
#     reverse_a = reverse_a * 10 + last_digit
#     temp = temp // 10
# print(reverse_a)

#  method - 02--------------
# Convert to string, reverse using [::-1], and convert back to int

num = int(input('Enter the number: '))
reversed_num = int(str(num)[::-1])    # works on stings data [start:stop:step]/ [: : -1] to reverse the string
print(type(reversed_num))