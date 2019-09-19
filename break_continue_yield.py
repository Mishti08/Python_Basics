"""
Python has break statement,continue statement, yield statement,pass statement
to use in loop for different reasons
Note: break,continue works for "for loop, for-if loop,while loop and while-if loop".
      Yield statement is for function return.
      The else block of for loop and while loop will execute only when the loop is "not" terminated by break statement.
"""

"""
Break statement
1. Exit the loop when break keyword is encountered.
2. Used with for if-else combination.
3.In for loop after hitting break keyword loop exits due to which else loop will not execute.
"""
#Example_1 break statement in if loop:
value=10
if value==10:
   break
   
#Output
# SyntaxError: 'break' outside loop

#Example_2 break statement in for if loop combination:
for n in range(0, 6):
    for x in range(0, n):
        if n == 2:
            print( "Going to exit loop",n)
            break
    else:
        print("Executes for-else loop for",n)
        
#Output
#Executes for-else loop for 0
#Executes for-else loop for 1
#Going to exit loop 2
#Executes for-else loop for 3
#Executes for-else loop for 4
#Executes for-else loop for 5

#Example_3 break statement in for loop after hitting break keyword loop exits due to which else loop is not executed:
list_value=[1,2,"a","b"]
for item in list_value:
    print("Item :",item)
    break
else:
    print("Else loop executed")
      
#Output
# Item :1

"""
Continue statement
1.Continue statement return control to beginning of loop when continue keyword is hit.
"""
#Example_1:
list_value=[1,2,"a","b"]
for item in list_value:
    print("Item :",item)
    continue
else:
    print("Else loop executed")

#Output
# Item : 1
# Item : 2
# Item : a
# Item : b
# Else loop executed

#Example_2:
number =2  
if number ==2:
    continue
else:
    print("Else loop")
            
#Output
# SyntaxError: 'continue' not properly in loop

#Example_3:
number =2
while number<5:
	if number ==2:
		continue
else:
    print("Out of for loop",number)
 
#Output
# Infinite loop

"""
Yield Statement is similar to return statement of a function.
1.Yield keyword suspends execution of function.
2.Yield keyword holds the last value of function before suspending the execution.
3.Yield is a generator it creates generator object on which iteration can be performed.
4.Yield holds value but doesn't consumes memory.
5.Because of point 4 yield can be iterated once only.
"""

#Example_1:
def num():
   for i in range(0,2):
      yield i**2
      
yield_value = num()  
print("Yield creates object:",yield_value)
   
#Output
# Yield creates object: <generator object num at 0x000001A2E5B6D0A0>


"""
Pass Statement
1.Pass statement is used to create empty loops.
2.If no statement is written or you want to do something later use pass keyword
3.It will create loop but wont throw error.
"""
#Example_1:
def num():
   for i in range(0,2):
      pass
      
pass_value = num()  
print("Yield creates object:",pass_value)

#Example_2 if-else loop with pass statement "Loop got exited after hitting pass so else loop also not got executed":
a=2
if a==2:
   print("If loop got executed:",a)
	pass
else:
	print("Loop got exited after hitting pass so else loop also not got executed")

   
#Output
# If loop got executed : 2
