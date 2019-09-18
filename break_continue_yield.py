"""
Python has break statement,continue statement, yield statement,pass statement
to use in loop for different reasons
"""

"""
Break statement
1. Exit the loop when break keyword is encountered.
2. Used with for if-else combination.
"""
Example_1 break statement in if loop:
value=10
if value==10:
   break
   
#Output
# SyntaxError: 'break' outside loop

Example_2 break statement in for if loop combination:
for n in range(0, 6):
    for x in range(0, n):
        if n == 2:
            print( "Going to exit loop",n)
            break
    else:
        # loop fell through without finding a factor
        print("Executes for-else loop for",n)
        
#Output
#Executes for-else loop for 0
#Executes for-else loop for 1
#Going to exit loop 2
#Executes for-else loop for 3
#Executes for-else loop for 4
#Executes for-else loop for 5

