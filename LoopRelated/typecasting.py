age = int(input('Please enter your age: '))
weight = float(input('Enter your weight: '))

if age <= 18:
    print("Sorry! you'r under age to purchase game.")
else:
    print("Welcome! you can purchase.")

print('Your age is: ' ,age)
print (type(age))    
    
print('Your weight is:', weight)
print(type(weight))

print('---------------after typecasting-------------')
new_age = str(age)
new_weight = str(weight)
print(type(new_age))
print(type(new_weight))