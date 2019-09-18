"""
Python has different types of loop
1.Iterative loops
    1.for loop
    2.while loop
    
2.Decision making loops
    1.if
    2.if else
    3.if elif else
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
#range(start_value,end_value,step=1) where range permits (end_value-1).Example:range(0,5)->0,1,2,3,4
#Step in range() means how much difference it should take for next count.Example:range(0,10,2)->0,2,4,6,8
#By default step in range() will be 1.
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

"""
If loop:
    1.Syntax: if (___) :
    2.Used for decision making.
    3.If loop will execute only if the condition is satisfied otherwise it will exit the loop.
"""
#Example_1:
#create if loop
#range(start_value,end_value,step=1) where range permits (end_value-1).Example:range(0,5)->0,1,2,3,4
#Step in range() means how much difference it should take for next count.Example:range(0,10,2)->0,2,4,6,8
if value in range(0,5):
    print("Value exists:",value)
    
#Output:
# NameError: name 'value' is not defined

#Example_2:
#create if loop
a=1
if value in range(0,5):
    print("Value exists:",value)
    
#Output:
# Value exists: 1

"""
If else loop:
    1.Syntax: if (___) :
                statement
              else
                statement
    2.Used for decision making.
    3.If loop will execute only if the condition is satisfied otherwise it will execute else loop and exit.
"""
#Example_1:
#create if else loop
#range(start_value,end_value,step=1) where range permits (end_value-1).Example:range(0,5)->0,1,2,3,4
#Step in range() means how much difference it should take for next count.Example:range(0,10,2)->0,2,4,6,8
if value in range(0,5):
    print("Value exists:",value)
else:
    print("Else loop will also not executes as value has name error")
#Output:
# NameError: name 'value' is not defined

#Example_2:
#create if else loop
a=12
if value in range(0,5):
    print("Value exists:"value)
else:
    print("Else loop will get executed as value has higher value than required for condition to satisfy")    
#Output:
# Else loop will get executed as value has higher value than required for condition to satisfy


"""
If elif else loop:
    1.Syntax: if (___) :
                statement
              elif (___):
                statement
              else
                statement
    2.Used for decision making.
    3.If loop will execute only if the condition is satisfied otherwise 
    it will check for elif condition if the condition is satisfied elif loop executes
    otherwise it will execute else loop and exit.
"""
#Example_1:
#create if elif else loop
#range(start_value,end_value,step=1) where range permits (end_value-1).Example:range(0,5)->0,1,2,3,4
if value in range(2,5):
    print("Value exists:"value)
elif value in range(0,5):
    print("Value exists:",value)
else:
    print("Else loop will also not executes as value has name error")
#Output:
# NameError: name 'value' is not defined

#Example_2:
#create if elif else loop
a=3
if value in range(5,10):
    print("Value exists:"value)
elif value in range(1,5):
    print("Value exists in elif condition:",value)
else:
    print("Else loop will also not executes as value has name error")
    
#Output
# Value exists in elif condition: 3

#Example_3:
#create if elif else loop
a=12
if value in range(0,5):
    print("Value exists:"value)
elif value in range(5,11):
    print("Value exists:",value)
else:
    print("Else loop will also not executes as value has name error")
    
#Output
# Else loop will also not executes as value has name error
