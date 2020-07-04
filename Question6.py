"""
Create a list with the names of friends and colleagues.
Search for the name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
"""


def searchName(input_list):
    for name in input_list:
        if name == 'John':
            return 'Name Found'
    return 'Name not Found'


name_list = ['Sujan', 'Sujal', 'Sanjit', 'Saujan', 'Saurav']
print(searchName(name_list))
