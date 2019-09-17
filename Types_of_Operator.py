"""
Python has operators similar to other languages.
  1.Arithmetic Operator(+,-,*,/,//,**)
  2.Logical Operator(AND,OR,NOT)
  3.Comparison Operator(<,>,<=,>=)
  4.Assignment Operator(=)
  5.Identity Operator(is,is not)
  6.Membership Operator(in, not in)
  7.Bitwise Operator(BitwiseAND,BitwiseOR,BitwiseNOT)
"""
 
"""
Arithmetic Operator(+,-,*,/,//,**)
"""
#Example:
a = 5
b = 10
sum= a+b
print("Sum is:",sum)
#Output
# Sum is : 15
sub= a-b
print("Subtraction is:",sub)
#Output
# Subtraction is: -5
div_float= a/b
print("Divison returns float value:",div_float)
#Output
# Divison returns float value: 0.5
div= a//b
print("Division returns integer value:",div)
#Output
# Division returns integer value: 0
mul= a*b
print("Multiplication is:",mul)
#Output
# Multiplication is: 50
power=a**b
print("Power is:",power)
#Output
# Power is:9765625

"""
Logical Operator(AND,OR,NOT)
"""
#Example:
non_zero_value= 5
zero_value = 0
#AND logic left to right if first value is non zero then only it will check for the second one.
AND_logic = non_zero_value and zero_value
print("AND_logic:",AND_logic)
#Output
# AND_logic: 0
#ORlogic left to right if first value is zero still it will check for the second one.
OR_logic = non_zero_value or zero_value
print("OR_logic:",OR_logic)
#Output
# OR_logic: 5
NOT_logic = not non_zero_value
print("NOT_logic :",NOT_logic)
#Output
# NOT_logic : False
NOT_logic = not zero_value
print("NOT_logic :",NOT_logic)
#Output
# NOT_logic : True

"""
Comparison Operator(<,>,<=,>=,==)
"""
#Example:
compare_a = 15
compare_b = 50
#Greater than
Greater_than = compare_a>compare_b
print("Greater_than:",Greater_than)
#Output
# Greater_than :False

#Lesser than
Lesser_than = compare_a>compare_b
print("Lesser_than:",Lesser_than)
#Output
# Lesser_than:True

#Greater than equal to
Grt_equ = compare_a>=compare_b
print("Greater than equal to",Grt_equ)
#Output
# Greater than equal to:False

#Lesser than equal to 
Less_equ = compare_a>=compare_b
print("Lesser than equal to:",Less_equ)
#Output
# Lesser than equal to:True

#Equal to
equ_to=(compare_a==compare_b)
print("Equal to:",equ_to)
#Output
# Equal to:False

"""
Assignment Operator(=)
"""
assign_a=10
assign_b= assign_a
print("assign_a :",assign_a)
print("assign_b :",assign_b)
#Output
# assign_a :10
# assign_b :10

"""
Identity Operator(is,is not)
"""
#Example:
id_1 = 5
id_2 = id_1
check_id= id_2 is id_1
print("Check address values match or not:",check_id)
print("Address of id_1:",id_1)
print("Address of id_2:",id_2)
#Output 
#Check address values match or not: True
#Address of id_1: 1865248512
#Address of id_2: 1865248512

check_id = id_2 is not id_1
print("Check address values match or not:",check_id)
#Output 
#Check address values match or not: False

"""
Membership Operator(in, not in)
"""
member_a = "Python"
member_b = "P"
check_belong = member_b in member_a
print("Check belongs to:",check_belong)
#Output
# Check belongs to: True
check_belong = member_b not in member_a
print("Check belongs to:",check_belong)
#Output
# Check belongs to: False

"""
Bitwise Operator(BitwiseAND,BitwiseOR,BitwiseNOT)
"""
bitwise_opt1 = 1 #binary 0001
bitwise_opt2 = 2 #binary 0010
bit_OR = bitwise_opt1 | bitwise_opt2
print("Bitwise OR:",bit_OR)
#Output
# Bitwise OR: 3
bit_AND = bitwise_opt1 & bitwise_opt2
print("Bitwise AND:",bit_AND)
#Output
# Bitwise AND: 0
bit_NOT = ~bitwise_opt1
print("Bitwise NOT:",bit_NOT)
#Output
# Bitwise NOT: -2

############Important Difference between is and == ###########################
"""
is operator verifies address/location
== operator verifies value
"""
is_op = "Python_operator"
eq_op = "Python_operator"
verify = is_op
#For string,integer,float is and == behave normally
str_verify_is = is_op is eq_op
str_verify_eq = (is_op == eq_op)
verify_val = is_op is verify
print("Verify is on string:",str_verify_is)
print("Verify == on string:",str_verify_eq)
print("Verify:",verify_val)
#Output
#Verify is on string: True
#Verify == on string: True
#Verify: True
"""
#For list it behaves differently because 
#List1 creates an object Obj1
#List2 creates an object Obj2
#List3 points to List1  Obj1
"""
List1 =[1,2,3]
List2 = [1,2,3]
List3 = List2
list_verify_is = List1 is List2
list_verify_eq = (List1 == List2)
verify_list = List1 is List3
print("Verify is on list:",list_verify_is)
print("Verify == on list:",list_verify_eq)
print("Verify:",verify_list)
#Output
#Verify is on list: False
#Verify == on list: True
#Verify: True
