# capitalize()
a = 'hello world python'
print('capitalized: ' ,a.capitalize())

# title()
print('titled: ', a.title())

# swapcase()
b = 'heLLo WorlD'
print('swapcase: ', b.swapcase())

# casefold()  # use for lowercase but more power full for special word: -> groß
c = 'groß'
print('casefold: ', c.casefold())

# replace()     # we can replace(old, new, count) either by indexing or exact value
d = 'Hellp'
print('replace: ',d.replace(d[-1], 'o'))
print('another replace: ',d.replace('l', 'k', 2))  

# count()
print('count: ',d.count('l'))

# isdigit()
e = 'H10' 

f = '10'
print('isdigit? ',e.isdigit())
print('isdigit? ',f.isdigit())

# join()    join() --> list to sting  &  split() --> string to list
g = ['h','e','l','l','o' ]
print(''.join(g))
h= ['1','2', '3']
print(''.join(h))
print(type(g))


