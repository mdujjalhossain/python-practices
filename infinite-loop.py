#  infinite loop only works in while loop

# a = 0
# while a <= 10:
#     a = a+1         # must use increment to stop infinite loop in while loop
#     print(a)




while True:
    user = input('Enter you name: ')
    if user == 'Quit' or user == 'q':
        print('Goodbye!')
        break
    print(f'Hi! {user}, good morning')