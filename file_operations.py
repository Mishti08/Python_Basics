"""
Python File Operation
1.  Open  Syntax :: open("file path with file file name and extension",mode_read/write/append)
2.  Read  
3.  Write
4.  Append
5.  Close

Note:: Close the file whenever you open it.
"""

#Example_1 open file:
open_file = open("file_operation.txt","r")
print("Opening a file creates Input output wrapper which allows to iterate over file :",open_file)
close_file = open_file.close()
print("Closing the open file :",close_file)

#Output
#   Opening a file creates Input output wrapper which allows to iterate over file : <_io.TextIOWrapper name='file_operation.txt' mode='r' encoding='cp1252'>
#   Closing the open file : None

#Example_2 read file:
open_file = open("file_operation.txt","r")
read_file = open_file.read()
print("Reading an open file  :",read_file)

#Output
#   Reading an open file  : Hi All
#   This is python tutorail for quick revision.
#   Keeping the file very simple.
#   But,as we learn more file complexity will increase.
#   Thanks.

#Example_3 write to file:
open_file = open("file_operation.txt","w")
write_file = open_file.write("Hi file got updated")
print("Writing an open file returns the number of characters written :",write_file)
print("Open the file and see the updated text")

#Output
#   Writing an open file returns the number of characters written  : 19
#   Open the file and see the updated text

#Example_4 append to file will not modify the whole file:
open_file = open("file_operation1.txt","a")
print("Opening a file creates Input output wrapper which allows to iterate over file :",open_file)
append_file = open_file.write("Hi file got updated at the last line.")
print("Writing an open file returns the number of characters written :",append_file)
print("Open the file and see the updated text")

#Output
#   Opening a file creates Input output wrapper which allows to iterate over file : <_io.TextIOWrapper name='file_operation1.txt' mode='a' encoding='cp1252'>
#   Writing an open file returns the number of characters written : 37
#   Open the file and see the updated text
