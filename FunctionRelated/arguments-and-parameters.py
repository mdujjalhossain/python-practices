# arguments and parameters in function

def greeting(name = 'Munna', days = 30):       # here is a and b is parameters (with value assigned= default parameters)
    print(f'Hello {name}! Your days strick is {days} days.')
    
greeting()
greeting('Korim', 15)                       # arguments value is more powerful then default parameter's value
greeting(name = 'Halima', days = 18)        # here Halima and 18 is arguments of name and days parameters
