# Task: Write a program to take integer input from user and display the grade according to the following criteria:
#       Marks  		      grade
#       >90		            A
#       >80 and <=90 	    B
#       >=60 and <=80	    C
#       below 60	        D


marks = int(input('Enter your marks to know grade: '))

if marks > 90:
    print('Your grade is A')
elif marks > 80 and marks <= 90:
    print('Your grade is B')
elif 60 <= marks <= 80:
    print('Your grade is C')
else:
    print('Your grade is D')