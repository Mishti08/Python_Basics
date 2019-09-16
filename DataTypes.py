"""
Python version 3.7
Data types in python are of 2 types
1.Mutable Datatype : data which can be modified at run time
Example: Dictionary,List,Set.

2.Immutable Datatype:data which can not be modified at run time
Example: FrozenSet,Integer,String,Float,Tuple.
"""
################## Mutable Datatype #####################
"""
List : 
  1.Format of creating list is [] or list().
  2.List has index and is similar to array in C.
  3.List is accessed using "index number".
  4.Updating a value of list is possible.
  5.Left to right and right to left values can be updated.
  6.List is ordered.
  7.List can have any datatype.
  8.List index start from "Zero".
  9.Maximum size of list :32-bit system(536,870,912)
"""
#Create list
List_create=["a",1,"e",5,"i",5.2]
#Update list
List_create[3]="updated"
#Output: 
#List_create = ['a', 1, 'e', 'updated', 'i', 5.2]

"""
Dictionary : 
  1.Format of creating dictionary is {} or dict().
  2.Dictionary has key and value pair.
  3.Dictionary is accessed using "key".
  4.Updating a value of dictionary is possible.
  5.Keys can't be updated.
  6.Dictionary is unordered.
  7.Dictionary can have any datatype.
"""
#Create Dictionary
dictionary={"a":1,"b":2,"c":3,4:"d"}
#Update Dictionary
dictionary["a"]=5
#Output :
#dictionary = {'a': 5, 'b': 2, 'c': 3,4:'d'}

"""
Sets : 
  1.Format of creating set is {} or set().
  2.Set needs update/add function to update.
  3.Set appends the value.
  4.Can't update set for a particular index.
  5.Set allow duplicates while creation but while printing it will remove duplicates.
  6.Set is unordered.
  7.Set can have any datatype.
"""
#Create Set
set_create={"a",1,10.2,"z"}
#Update Set
set_create.add("z")
#Output :
#set_create = {'z', 1, 10.2, 'a'}

##################Immutable Datatype ##########################
"""
Integers : 
  1.Format of creating integer is just writing it.
  2.Python is dynamically typed language which allows programmers to not specify the type of data.
  3.Integers have in-built int() function working in backend.
  4.Can't update int for a particular index.
  5.Maximum size of integer:32-bit = 2^31-1(2,147,483,647)
"""
#Create Integer
int_create = 50
#Output :
#int_create = 50
#Update Integer
int_create[0]= 1
#Output :
#TypeError: 'int' object does not support item assignment
int_create = 60
#Output :
#int_create = 60

"""
String : 
  1.Format of creating string is just writing it with "" or '' or """ """.
  2.Python is dynamically typed language which allows programmers to not specify the type of data.
  3.String have in-built str() function working in backend.
  4.Can't update str for a particular index.
  5.Size of string depends on RAM of system.
"""
#Create String
str_create = "Python"
#Output :
#str_create = 'Python'
#Update String
str_create[0] = "C"
#Output :
#TypeError: 'str' object does not support item assignment
str_create = "Cython"
#Output :
#str_create = 'Cython'

"""
FrozenSet : 
  1.Format of creating frozenset is frozenset().
  2.FrozenSet are fixed and can't be modified.
"""
#Create FrozenSet
frozen_set=frozenset("a","b",100)
#TypeError: frozenset expected at most 1 arguments, got 3
argument=[1,2]
frozen_set=frozenset(argument)
#Output:
#frozen_set = frozenset({1, 2})
#Update FrozenSet
argument1=("a","b")
frozen_set=frozenset(argument1)
#Output:
#frozen_set = frozenset({'a','b'})
