# method- 1: Format function------------
name = 'Rahim'
age = 20

info= 'I am {}. I am {} years old'.format(name, age)      # approach --- 1
print(info)

info2 = 'I am {0}. I am {1} years old'.format(name, age)     # approach --- 2
print(info2)


# method- 2: f-string

print(f'I am {name}. I am {age} years old.')