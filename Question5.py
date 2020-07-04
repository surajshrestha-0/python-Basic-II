"""
Create a tuple with your first name, last name, and age.
Create a list, people, and append your tuple to it.
Make more tuples with the corresponding information from your friends and append them to the list.
Sort the list.
When you learn about sort method, you can use the key parameter to sort by
any field in the tuple, first name, last name, or age.
"""
name_tuple = ('Suraj', 'Shrestha', 22)
people = []

# appending name_tuple to empty list
people.append(name_tuple)
print(people)

# appending information from friends
people.append(('Ram', 'Shahi', 20))
people.append(('Shyam', 'Chhetri', 19))
people.append(('Binod', 'Dangol', 24))
people.append(('Krishna', 'Shakya', 24))

# sorted list based on first name
print(sorted(people, key=lambda x: x[0]))
# sorted list based on last name
print(sorted(people, key=lambda x: x[1]))
# sorted list based on age
print(sorted(people, key=lambda x: x[2]))
