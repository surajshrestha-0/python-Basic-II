"""
Write a function to write a comma-separated value (CSV) file.
It should accept a filename and a list of tuples as parameters.
The tuples should have a name, address, and age. The file should create
a header row followed by a row for each tuple. If the following list of
tuples was passed in:
[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
it should write the following in the file:
name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
"""
import csv


def csvWriter(filename, list_of_tuple):
    file_name = filename + '.csv'
    with open(file_name, 'w', newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['name', 'address', 'age'])
        for row in list_of_tuple:
            csv_out.writerow(row)


data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
name = 'person'
csvWriter(name, data)
