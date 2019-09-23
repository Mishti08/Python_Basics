
"""
Python dictionary comprehension
1.Its an alternative to lambda function.
2.If there is nested loops which are confusing use of dictionary comprehension makes it easy to to understand.
"""
#Example_1 without dictionary comprehension:
create_dictionary = {1:"Python",2:"is",3:"easy",4:"language"}
for item,name in create_dictionary.items():
    print("Dictionary :",item,name)

#Output:
#   Dictionary : 1 Python
#   ictionary : 2 is
#   Dictionary : 3 easy
#   Dictionary : 4 language

#Example_2 with dictionary comprehension:
create_dictionary = {1:"Python",2:"is",3:"easy",4:"language"}
dict_comprehension = {(key,value) for key,value in create_dictionary.items() }
print("Dictionary with comprehension separated like (key,value):",dict_comprehension)

dict_comprehension = {key:value for key,value in create_dictionary.items() }
print("Dictionary with comprehension separated like (key:value):",dict_comprehension)

#Output
#   Dictionary with comprehension separated like (key,value): {(1, 'Python'), (2, 'is'), (3, 'easy'), (4, 'language')}
#   Dictionary with comprehension separated like (key:value): {1: 'Python', 2: 'is', 3: 'easy', 4: 'language'}
