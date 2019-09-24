"""
Python context manager for file operation

"with" keyowrd is used for file operations which closes file itself
Syntax  ::  with open(filename,mode) as new_IOwrapper_name
"""
#Example_1:
with open("file_operation.txt","r") as read_file:
    read_line = read_file.readlines()
    print("Reading line by line and storing in a list :",read_line)

print("IOTextWrapper of file:",read_file)

#Output
#   Reading line by line and storing in a list : ['Hi All\n', 'This is python tutorail for quick revision.\n', 'Keeping the file very simple.\n', 'But,as we learn more file complexity will increase.\n', 'Thanks.']
#   IOTextWrapper of file: <_io.TextIOWrapper name='file_operation.txt' mode='r' encoding='cp1252'>
