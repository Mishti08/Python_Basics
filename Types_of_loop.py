"""
Python has different types of loop
1.for loop
2.while loop
"""
"""
For loop:
    1.Syntax: for (___) in (___):
    2.Used for iteration.
    
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
#             'a'
#             'b'

#Example_3:
#create for loop
#Iterating over a dictionary
dict_value={1:"Hi",2:"Python","a":3,"b":0}
for value in dict_value.items():
    print(value)
    
#Output:
#value =     (1, 'Hi')
#            (2, 'Python')
#            ('a', 3)
#            ('b', 0)
    
