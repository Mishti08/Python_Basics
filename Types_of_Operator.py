"""
Python has operators similar to other languages.
  1.Arithmetic Operator(+,-,*,/,//,**)
  2.Logical Operator(AND,OR,NOT)
  3.Comparison Operator(<,>,<=,>=)
  4.Assignment Operator(=)
  5.Identity Operator(is,is not)
  6.Membership Operator(in, not in)
  
"""
 
"""
Arithmetic Operator(+,-,*,/,//,**)
"""
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
Comparison Operator(<,>,<=,>=)
"""
