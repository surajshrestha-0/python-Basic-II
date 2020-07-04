"""
Create a list of tuples of first name, last name, and age for your friends and colleagues.
If you don't know the age, put in None.
Calculate the average age, skipping over any None values.
Print out each name, followed by old or young if they are above or below the average age.
"""

from statistics import mean


def averageAge(input_list):
    age_list = []
    for values in input_list:
        if values[2] is not None:
            age_list.append(values[2])
    return mean(age_list)


name_list = [('Ram', 'Shahi', 20), ('Shyam', 'Chhetri', None), ('Binod', 'Dangol', 24),
             ('Krishna', 'Shakya', None), ('Raju', 'Thapa', 20), ('Roman', 'Shrestha', 20)]
print(averageAge(name_list))
