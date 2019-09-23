"""
Python input function to take input from user
input() always returns string

"""
#Example_1:
name = input("Enter your name:")
print("Entered name is",name)

#Output
#   Enter your name:Python
#   Entered name is Python

#Example_2:
number = input("Enter your favourite number:")
print("Entered number is",number)
print("type of number:",type(number))
add = number + number
print("Now enetered value can not be used as int:",add)

#Output
#   Enter your favourite number:55
#   Entered number is 55
#   type of number: <class 'str'>
#   Now enetered value can be used as int: 5555

#Example_3:
number = int(input("Enter your favourite number:"))
print("Entered number is",number)
print("type of number:",type(number))
add = number + number
print("Now enetered value can be used as int:",add)

#Output
#   Enter your favourite number:55
#   Entered number is 55
#   type of number: <class 'int'>
#   Now enetered value can be used as int: 110
