# break keyword----------

# for i in range(10):
#     # print(i)      # this will print with 5 as before checking the break 
#     if i == 5:
#         break
#     print(i)        # this will print without 5 after checking the break 
    

# continue keyword ---------
# for i in range (10):
#     # print(i)      # this will print with 5 as before checking the continue 
#     if i == 5:
#         continue
#     print(i)        # this will skip the 5 and print rest of the numbers to continue    

a = 0
while a <= 10:
    a = a + 1
    if a == 5:
        continue
    print(a)