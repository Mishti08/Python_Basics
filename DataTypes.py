"""
Python version 3.7
Data types in python are of 2 types
1.Mutable Datatype : data which can be modified at run time
Example: Dictionary,List,Set.

2.Immutable Datatype:data which can not be modified at run time
Example: FrozenSet,Integer,String,Float,Tuple.
"""
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
#Create dictionary
dictionary={"a":1,"b":2,"c":3,4:"d"}
#Update Dictionary
dictionary["a"]=5
#Output :
#dictionary = {'a': 5, 'b': 2, 'c': 3,4:'d'}

