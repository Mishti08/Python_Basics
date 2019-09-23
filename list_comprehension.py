"""
Python list comprehension
1.Used for storing result in a list after performing some operation.
2.List comprehension reteuns a list.
3.List comprehension is more compact and faster than normal functions and loops for creating list.
Syntax: 
    [      inside this braces we can give conditins     ]

Example:  [output_if_condition_pass     condition       output_if_condition_fails]
"""
#Example_1 without list comprehension:
create_list=[]

for item in range(1,11):
    table=item*2
    create_list.append(table)

# print("List updated for creating a table of 2:",create_list)

#Output:
#   List updated for creating a table of 2 :[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Example_2 with list comprehension:
create_list = [item*2 for item in range(1,11)]
print("List updated for creating a table of 2:",create_list)

#Output:
#   List updated for creating a table of 2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Example_3 with list comprehension:
create_list = [print("Char is present") if "P" in "Python" else  print("Char is not present")]

create_list1 = [print("Char is present") if "k" in "Python" else  print("Char is not present")]

#Output
# Char is present
# Char is not present
