# [Expression (element) for element in list: (if condition)] like-> i for i in list/range

# Example-4: Using if with list comprehension
a = []
for i in range(1, 10):
    if i % 3 == 0:
        a.append(i)
print(a)        # using loop 

b = [i for i in range(1, 10) if i % 3 ==0]
print(b)        # using list comprehension


# Example-5: Nested if with list comprehension
a = []
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:    # multiple condition in a single statement
        a.append(i)
    # if i % 5 == 0:
    #     a.append(i)       # multiple if statement inside a loop [doing the similar like above]
print(a)

b = [i for i in range(1, 11) if i % 3 == 0 or i % 5 == 0]       # same output doing the list comprehension
print(b)


# Example-6: if...else with list comprehension [if else for i in list/range]
a = []
for i in range(1, 10):
    if i % 2 == 0:
        a.append('Even')
    else:
        a.append('Odd')
print(a)

b =["Even" if i % 2 == 0 else "Odd" for i in range(1, 10)]      # if statement first then condition
print(b)








