"""
Python functions
Syntax for function definition:
  def fun_name(argument1,argument2):
    statement
def keyword represents function
Syntax for function call:
  fun_name(argument1,argument2)
"""

#Example_1 function with default arguments:
def add():
    print("add function without arguments")
    
add()
#Output
# add function without arguments

#Example_2 function with keyword arguments and without return keyword:
def add(val1,val2):
    print("Addition starts")
    sum = val1+val2
    print("add function with arguments")
    
store_add = add(5,4)
print("Store_add got created but holds no value as function is not returning any value",store_add)
#Output
#Addition starts
# add function with arguments
# Store_add got created but holds no value as function is not returning any value

#Example_3 function with keyword arguments and with return keyword:
def add(val1,val2):
    print("Addition starts")
    sum = val1+val2
    print("add function with arguments")
    return sum
    
store_add = add(5,4)
print("Store_add got created and holds return value:",store_add)
#Output
#Addition starts
# add function with arguments
# Store_add got created and holds return value:9

#Example_4 function with default argument and keyword arguments and with return keyword:
def add(val1=5,val2):
    print("Addition starts")
    sum = val1+val2
    print("add function with arguments")
    return sum
    
store_add = add(4)
print("Store_add got created and holds return value:",store_add)
#Output
#SyntaxError: non-default argument follows default argument

#Example_5 function with default argument and keyword arguments and with return keyword:
#Precedence of keyword argument is high than default argument
#So,always use def fun_name( keyword argument,default argument) to prevent error.
def add(val1,val2=10):
    print("Addition starts")
    sum = val1+val2
    print("add function with arguments")
    return sum
    
store_add = add(val1= 4)
print("Store_add got created and holds return value:",store_add)
#Output
#Addition starts
# add function with arguments
# Store_add got created and holds return value: 14
