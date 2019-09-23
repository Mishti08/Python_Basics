"""
Python list operations
1.  append      will add in last.
2.  extend      will increase the list using iterable.
3.  insert      will insert value at any index.
4.  remove      will remove any index value by giving the value. 
                if value have 2 occurences 1st occurence will be removed,
5.  pop         will pop out like stack.
6.  index       search for value in list and return the index number if present else thrwos error.
7.  count       count the number of values present.
8.  del         delete the index value if given else delete whole list.
9.  reverse     reverse the list. 
10. copy        craetes a copy of list(shallow copy).
"""
############## Append Operation #################

#Example_1   Syntax :: list.append(value to add):

create_list= ["Python","version"]
create_list.append(3.6)
print("List after append operation:",create_list)

#Output
#   List after append operation: ['Python', 'version', 3.6]

#Example_2   Syntax :: list.append(value to add):
create_list = []
for item in range(1,10):
    create_list.append(item)
    print("List after append operation:",create_list)

#Output
#   List after append operation: [1]
#   List after append operation: [1, 2]
#   List after append operation: [1, 2, 3]
#   List after append operation: [1, 2, 3, 4]
#   List after append operation: [1, 2, 3, 4, 5]
#   List after append operation: [1, 2, 3, 4, 5, 6]
#   List after append operation: [1, 2, 3, 4, 5, 6, 7]
#   List after append operation: [1, 2, 3, 4, 5, 6, 7, 8]
#   List after append operation: [1, 2, 3, 4, 5, 6, 7, 8, 9]

############## Extend Operation #################
#Example_1   Syntax :: list.extend(value to add from iterable):
create_list = []

create_list.extend(range(1,10))
print("List after extend operation:",create_list)

#Output
#   List after extend operation: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Example_2   Syntax :: list.extend(value to add from iterable):
create_list = ["Python","Learn"]
list_join = ["Easy","Features"]
create_list.extend(list_join)
print("List after extend operation:",create_list)

#Output
#   List after extend operation: ['Python', 'Learn', 'Easy', 'Features']

############## Insert Operation #################
#Example_1   Syntax :: list.insert(index_number,value to add from iterable):

create_list = []
create_list.insert(0,"Python")
print("List after insert operation:",create_list)

#Output
#   List after insert operation: ['Python']

#Example_2   Syntax :: list.insert(index_number,value to add from iterable):
create_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
create_list.insert(5,"Python")
print("List after insert operation:",create_list)

#Output
#   List after insert operation: [1, 2, 3, 4, 5, 'Python', 6, 7, 8, 9]

############## Remove Operation #################
#Example_1   Syntax :: list.insert(value to remove):

create_list = [1, 2, 3, 4, 5, 'Python', 6, 7,'Python', 8, 9]
create_list.remove('Python')
print("List after remove operation:",create_list)

#Output
#   List after remove operation: [1, 2, 3, 4, 5, 6, 7, 'Python', 8, 9]

############## Pop Operation #################
#Example_1   Syntax :: list.pop(index to remove):
create_list = [1, 2, 3, 4, 5, 'Python', 6, 7,'Python', 8, 9]
create_list.pop(-1)
print("List after pop operation:",create_list)

#Output
#   List after pop operation: [1, 2, 3, 4, 5, 'Python', 6, 7, 'Python', 8]

############## Index Operation #################
#Example_1   Syntax :: list.index(value to search in list and return the index number of it):
create_list = [1, 2, 3, "name",4, 5, 'Python', 6, 7,'Python', 8, 9]
print("List after index operation:",create_list.index("name"))

#Output
#   
#   List after index operation: 3

############## Count Operation #################
#Example_1   Syntax :: list.count(value to search in list and return the number of it):
create_list = [1, 2, 3, "name",4, 5, 'Python', 6, 7,'Python', 8, 9]
print("List after count operation:",create_list.count("Python"))

#Output
#   List after count operation: 2

############## Delete Operation #################
#Example_1   Syntax :: del list_name(index to delete):
create_list = [1, 2, 3, "name",4, 5, 'Python', 6, 7,'Python', 8, 9]
del (create_list[5])
print("List after del operation:",create_list)

#Output
#   List after del operation: [1, 2, 3, 'name', 4, 'Python', 6, 7, 'Python', 8, 9]

############## Reverse Operation #################
#Example_1   Syntax :: list.reverse():
create_list = [1, 2, 3, "name",4, 5, 'Python', 6, 7,'Python', 8, 9]
create_list.reverse()
print("List after reverse operation:",create_list)

#Output
#   List after reverse operation: [9, 8, 'Python', 7, 6, 'Python', 5, 4, 'name', 3, 2, 1]

############## Copy Operation #################
#Example_1   Syntax :: list.copy():
create_list = [1, 2, 3, "name",4, 5, 'Python', 6, 7,'Python', 8, 9]
copied_list = create_list.copy()
print("List after copy operation:",copied_list)

#Output
#   List after copy operation: [1, 2, 3, 'name', 4, 5, 'Python', 6, 7, 'Python', 8, 9]
