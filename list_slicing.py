"""
Python list slicing 
Python index starts from "zero".
Python index ends can be counted as negative values.
  0   1   2
--------------->  
["a","b","c"]
<---------------
 -3  -2   -1
"""
#Example_1 positive and negative slicing:
craete_list = ["a","b","c",10,20,30]
sliced_alpha = craete_list[0:3]
print("Sliced alphabets:",sliced_alpha)
sliced_num = craete_list[-3:]
print("Sliced numbers:",sliced_num)

#Output
#   Sliced alphabets: ['a', 'b', 'c']
#   Sliced numbers: [10, 20, 30]

#Example_2:
craete_list = ["a","b","c",10,20,30]
sliced = craete_list[1:4]
not_sliced = craete_list[0:]
print("Sliced list:",sliced)
print("Not sliced list:",not_sliced)

#Output
#   Sliced list: ['b', 'c', 10]
#   Not sliced list: ['a', 'b', 'c', 10, 20, 30]
