"""
Python has different types of loop
1.for loop
2.while loop
"""
"""
For loop:
    1.Syntax: for (___) in (___):
    2.Used for iteration.
    3.For loop can have else condition also it executes just after the for loop exit without "break" 
    (**but its not recommendable to use it).
    4.For loop is used when the number of iterations are known exactly.
"""
#Example_1:
#create for loop
#range(start_value,end_value) where range permits (end_value-1).Example:range(0,5)->0,1,2,3,4
for value in range(0,5):
    print(value)
    
#Output:
#Value =  0
#         1
#         2
#         3
#         4

#Example_2:
#create for loop
#Iterating over a list
list_value=[1,2,"a","b"]
for item in list_value:
    print(item)
    
#Output:
#item =        1
#              2
#              a
#              b

#Example_3:
#create for loop
#Iterating over a dictionary
dict_value={1:"Hi",2:"Python","a":3,"b":0}
#dict_value.items() allows iteration over dictionary items
for value in dict_value.items():
    print(value)
    
#Output:
#value =     (1, 'Hi')
#            (2, 'Python')
#            ('a', 3)
#            ('b', 0)
    
#Example_4:
#create for loop
#Iterating over a list and applying else loop
list_value=[1,2,"a","b"]
for item in list_value:
    print(item)
else:
    print("Else loop executed")
    
#Output:
#item =        1
#              2
#              a
#              b
#             Else loop executed

#Example_5:
#create for loop
#Iterating over a list and applying else loop
list_value=[1,2,"a","b"]
for item in list_value:
    print(item)
    break
else:
    print("Else loop executed")
    
#Output:
#item =        1 and it exited the loop

"""
While loop:
    1.Syntax: while (___):
    2.Used for looping till the condition is satisfied.
    3.While loop can have else condition also it executes just after the while loop exit without "break" 
    (**but its not recommendable to use it).
    4.While loop turns infinite if condition is not satisfied.
    5.While loop is used when the number of iteration are not known exactly.
"""
#Example_1:
#create while loop
#Loop till condition is satisfied
a=0
while a<5:
    print("Value of a:",a)
    a=a+1
    
#Output:
#   Value of a: 0
#   Value of a: 1
#   Value of a: 2
#   Value of a: 3
#   Value of a: 4

#Example_2:
#create while loop
#Infinite loop prints till program is not killed intentionally
while True:
    print("Infinite loop")
    
#Output:
#Infinite loop
#Infinite loop
#Infinite loop
#Infinite loop
#Infinite loop
#............. 

#Example_3:
#create while loop
#Loop till condition is satisfied and executes else loop
a=0
while a<5:
    print("Value of a:",a)
    a=a+1
else:
    print("Else loop executed")
#Output:
#   Value of a: 0
#   Value of a: 1
#   Value of a: 2
#   Value of a: 3
#   Value of a: 4
#   Else loop executed

#Example_4:
#create while loop
#Loop till break is hit and exits
a=0
while a<5:
    print("Value of a:",a)
    a=a+1
    break
else:
    print("Else loop executed")
#Output:
#   Value of a: 0

