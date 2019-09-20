"""
Python combinations of datatype
1.List inside Dictionary  {key:[values]}
2.Dictionary inside List  [value,{key:value}]
3.List inside set    {[list1],[list2]}
4.Set inside list    [{set1},{set2}]
5.List inside tuple  ([list1],[list2])
6.Tuple inside list  [(val1,val2),(val3,val4)]
7.Tuple inside Dictionary  {key:(values)}
and so many other combinations based on the need we can use the combination of datatypes
"""
"""
List inside Dictionary
1.Used when for one key you have to store lots of value
"""
#Example_1:
dictionary={}

dictionary["add_list"]=[5,4,"Python","is","simple"]
print(dictionary)
for key, value in dictionary.items():
    print(f"Key is {key} Value {value}")

#Output
#  {'add_list': [5, 4, 'Python', 'is', 'simple']}
#  Key is add_list Value [5, 4, 'Python', 'is', 'simple']

#Example_2:
dictionary={}


dictionary["add_list"]=[5,4,"Python","is","simple"]
dictionary["digit"] = 500
print(dictionary)
for key, value in dictionary.items():
    print(f"Key is {key} Value {value}")
    # isinstance will check that the value is a list or not basically it  checks for class here list is a class
    if isinstance(value, list):
        for search in value:
            print (f'Iterating for a list in {key}: {search}')
    else:
        print (f'Class type is not list {key}: {value}')


#Output
#   {'add_list': [5, 4, 'Python', 'is', 'simple']}
#   Key is add_list Value [5, 4, 'Python', 'is', 'simple']
#   Iterating for a list in add_list: 5
#   Iterating for a list in add_list: 4
#   Iterating for a list in add_list: Python
#   Iterating for a list in add_list: is
#   Iterating for a list in add_list: simple
#   Key is digit Value 500
#   Class type is not list digit: 500


"""
List inside Set
"""
#Example_1:
create_set = {5,4,3}
print(type(create_set))
#Output
#    <class 'set'>

#Example_2:
create_set = set(5,4,3,['Python', 'is', 'simple'])
print(type(create_set))
# Output
#   TypeError: unhashable type: 'list'

#Example_3:
create_set = set(['Python', 'is', 'simple'])
print(type(create_set))
for item in create_set:
    print("Iterating over list in set:",item)
#Output
#    <class 'set'>
#   Iterating over list in set: Python
#   Iterating over list in set: is
#   Iterating over list in set: simple

"""
List inside Tuple
"""

#Example_1:
create_tuple = ("Hi","Python","Developers")
print(type(create_tuple))
for item in create_tuple:
    print("Iterating over tuple:",item)

#Output
#   <class 'tuple'>
#   Iterating over tuple: Hi
#   Iterating over tuple: Python
#   Iterating over tuple: Developers

#Example_2:
create_tuple = tuple(['Python', 'is', 'simple'])
print(type(create_tuple))
for item in create_tuple:
    print("Iterating over list in tuple:",item)

#Output
#   <class 'tuple'>
#   Iterating over list in tuple: Python
#   Iterating over list in tuple: is
#   Iterating over list in tuple: simple

#Example_3:
create_tuple = tuple('Python', 'is', 'simple')
print(type(create_tuple))

#Output
#   TypeError: tuple expected at most 1 arguments, got 3

"""
List inside List
"""
#Example_1:
create_list =[]
create_list1 = [10,9,8,7,create_list]

print("List inside list:",create_list1)

#Output
#   List inside list: [10, 9, 8, 7, []]

#Example_2:
create_list =[]
create_list1 = [10,9,8,7,create_list]
for item in create_list1:
    print("List inside list:",item)

#Output
#   List inside list: 10
#   List inside list: 9
#   List inside list: 8
#   List inside list: 7
#   List inside list: []

"""
Dictionary inside List
"""

#Example_1:
create_list=["index0"]
create_list[0] = {"Hii":"Python","ver":3.0}
print(type(create_list))
print("List with dictionary",create_list)
for item in create_list:
    print("Item in list:",item)

#Output
#   <class 'list'>
#   List with dictionary [{'Hii': 'Python', 'ver': 3.0}]
#   Item in list: {'Hii': 'Python', 'ver': 3.0}

#Example_2:
create_list=[]
create_list[0] = {"Hii":"Python","ver":3.0}
print(type(create_list))

#output
#   IndexError: list assignment index out of range

#Example_3:
create_list=["add_dict","digit"]
create_list[0]={'Hii': 'Python', 'ver': 3.0}
create_list[1] = 500
print(create_list)
for index in create_list:
    # isinstance will check that the value is a dictionary or not basically it  checks for class here dictionary is a class
    if isinstance(index, dict):
        for search in index:
            print (f'Iterating over dictionary in list index {index}: key {search}')
    else:
        print (f'Class type is not dictionary {index}')

#Output
#   [{'Hii': 'Python', 'ver': 3.0}, 500]
#   Iterating over dictionary in list index {'Hii': 'Python', 'ver': 3.0}: key Hii
#   Iterating over dictionary in list index {'Hii': 'Python', 'ver': 3.0}: key ver
#   Class type is not dictionary 500

"""
Dictionary inside set
"""
#Example_1:
create_set = set(5,4,3,{'Hii': 'Python', 'ver': 3.0})
print(type(create_set))

# Output
#   TypeError: set expected at most 1 arguments, got 4

#Example_2:
create_set = set({'Hii': 'Python', 'ver': 3.0})
print(type(create_set))
for item in create_set:
    print("Iterating over dictionary keys in set:",item)
#Output
#    <class 'set'>
#   Iterating over dictionary keys in set: ver
#   Iterating over dictionary keys in set: Hii

#Example_3:
create_set = set({'Hii': 'Python', 'ver': 3.0})
create_set.add(500)
print("Added item to set:",create_set)
# Set dont provide index format to access variable

#Output
#   Added item to set: {'Hii', 500, 'ver'}

"""
Dictionary inside Tuple
"""
#Example_1:
create_tuple = tuple({'Hii': 'Python', 'ver': 3.0})
print(type(create_tuple))
for item in create_tuple:
    print("Iterating over dictionary in tuple:",item)

#Output
#   <class 'tuple'>
#   Iterating over dictionary in tuple: Hii
#   Iterating over dictionary in tuple: ver

"""
Dictionary inside Dictionary
"""
#Example_1:
create_dict = {'Hii': 'Python', 'ver': 3.0}
update_dict = {create_dict,{"learning":"Fun"}}
print(update_dict)

#Output
#   TypeError: unhashable type: 'dict'

#Example_2:
create_dict = {'Hii': 'Python', 'ver': 3.0,"change":""}
create_dict['change'] = {"Learn":"Python its easy"}
print("Dictionary as a value of key:",create_dict)

#Output
#   Dictionary as a value of key: {'Hii': 'Python', 'ver': 3.0, 'change': {'Learn': 'Python its easy'}}

"""
Set inside List
"""
#Example_1:
create_list=["add_dict","digit"]
create_list[1] = {5,4,9}
print("List includes set:",create_list)
print("Type of index 1:",type(create_list[1]))

#Output
#   List includes set: ['add_dict', {9, 4, 5}]
#   Type of index 1: <class 'set'>

#Example_2:
create_list=["add_dict","digit"]
create_list[1] = {5,4,9}
for item in create_list:
    print("Iteration over list with set in it:",item)
    if isinstance(item, set):
        for search in item:
            print (f'Iterating over set in list index {item}')
    else:
        print (f'Class type is not set {item}')

#Output
#   Iteration over list with set in it: add_dict
#   Class type is not set add_dict
#   Iteration over list with set in it: {9, 4, 5}
#   Iterating over set in list index {9, 4, 5}
#   Iterating over set in list index {9, 4, 5}
#   Iterating over set in list index {9, 4, 5}

"""
Set inside Dictionary
"""
#Example_1:
create_dict = {'Hii': 'Python', 'ver': 3.0}
create_dict['ver'] ={3.0,3.1,3.6,3.7}
print("Dictionary with set",create_dict)
print("Data Type of key 'ver'':",type(create_dict['ver']))

#Output
#   Dictionary with set {'Hii': 'Python', 'ver': {3.6, 3.0, 3.7, 3.1}}
#   Data Type of key 'ver'': <class 'set'>

#Example_2:
create_dict = {'Hii': 'Python', 'ver': 3.0}
create_dict['ver'] ={3.0,3.1,3.6,3.7}
for key,value in create_dict.items():
    print(f"Dictionary with Key: {key} Value: {value}")
    if isinstance(value, set):
        print (f'Iterating over set in a dictionary {key}: key {value}')
    else:
        print (f'Class type is not dictionary {key}')
#Output:
#   Dictionary with Key: Hii Value: Python
#   Class type is not dictionary Hii
#   Dictionary with Key: ver Value: {3.6, 3.0, 3.7, 3.1}
#   Iterating over set in a dictionary ver: key {3.6, 3.0, 3.7, 3.1}

"""
Set inside Tuple
"""
#Example_1:
create_tuple =tuple({5,4,3,2})
print("Type of tuple with set:",create_tuple)
for item in create_tuple:
    print("Iterate over set inside tuple:",item)

#Output
#   Type of tuple with set: (2, 3, 4, 5)
#   Iterate over set inside tuple: 2
#   Iterate over set inside tuple: 3
#   Iterate over set inside tuple: 4
#   Iterate over set inside tuple: 5

"""
Set inside Set
"""
#Example_1:
create_set ={1,2,3,4,{"A","B","C","D"}}
print("Type of set with set:",create_set)

#Output
#   TypeError: unhashable type: 'set'

#Example_2:
create_set ={1,2,3,4}
set_2 = {"A","B","C","D"}
final_set =set([create_set,set_2])
print("set with set:",final_set)

#Output
#   TypeError: unhashable type: 'set'

#Example_3 set inside set needs frozen set:
create_set =[1,2,3,4]
set_2 = ["A","B","C","D"]
final_set =set([frozenset(create_set),frozenset(set_2)])
print("Type of final set:",type(final_set))
print("Set contains:",final_set)

for item in final_set:
    print("Iteration on set:",item)

#Output
#   Type of final set: <class 'set'>
#   Set contains: {frozenset({'B', 'A', 'D', 'C'}), frozenset({1, 2, 3, 4})}
#   Iteration on set: frozenset({'B', 'A', 'D', 'C'})
#   Iteration on set: frozenset({1, 2, 3, 4})

"""
Tuple inside List
"""
#Example_1:
create_list= ["A","B","C","D"]
create_list[1] = tuple("Python")
print("Updated list with tuple:",create_list)
print("Type of list :",type(create_list[1]))

#Output
#   Updated list with tuple: ['A', ('P', 'y', 't', 'h', 'o', 'n'), 'C', 'D']
#   Type of list : <class 'tuple'>

#Example_2:
create_list= ["A","B","C","D"]
create_list[1] = tuple("Python")
for item in create_list:
    print("Iteration on list :",item)

#Output
#   Iteration on list : A
#   Iteration on list : ('P', 'y', 't', 'h', 'o', 'n')
#   Iteration on list : C
#   Iteration on list : D

"""
Tuple inside Dictionary
"""

#Example_1:
create_dict = {'Hii': 'Python', 'ver': 3.0}
create_dict['Hii'] = ('R','Python','Go')
print("Type of dictionary key  :",type(create_dict['Hii']))
print("Dictionary",create_dict)

#Output
#   Type of dictionary key  : <class 'tuple'>
#   Dictionary {'Hii': ('R', 'Python', 'Go'), 'ver': 3.0}

#Example_2:
create_dict = {'Hii': 'Python', 'ver': 3.0}
create_dict['Hii'] = ('R','Python','Go')
for key,value in create_dict.items():
    print(f"Dictionary iteration key {key} Value {value}")

#Output
#   Dictionary iteration key Hii Value ('R', 'Python', 'Go')
#   Dictionary iteration key ver Value 3.0

"""
Tuple inside Set
"""
value= tuple("Python")
create_set = {"A","B","C","D",value}
print("Set :",create_set)

#Output
#   Set :{'A', 'C', ('P', 'y', 't', 'h', 'o', 'n'), 'D', 'B'}

"""
Tuple inside Tuples
"""
#Example_1:
value= ("Python","Learning")
print("Type of value:",type(value))
new_tuple =("Easy","Effective")
final_tuple = (value,new_tuple)
print("Tuple with tuple:",final_tuple)

#Output
#   Type of value: <class 'tuple'>
#   (('Python', 'Learning'), ('Easy', 'Effective'))

#Example_2:
value= ("Python","Learning")
new_tuple =("Easy","Effective")
final_tuple = (value,new_tuple)
for item in final_tuple:
    print("Tuple iteration:",item)

#Output
#   Tuple iteration: ('Python', 'Learning')
#   Tuple iteration: ('Easy', 'Effective')
