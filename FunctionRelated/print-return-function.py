# print vs return in function

def sum(a,b):
    print(a+b)
sum(2,8)


def sum_with_return(a,b):
    return a+b
result = sum_with_return(4,8)
result += 12
print(result)