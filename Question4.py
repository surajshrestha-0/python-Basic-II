"""
Create a list.
Append the names of your colleagues and friends to it.
Has the id of the list changed?
Sort the list.
What is the first item on the list? What is the second item on the list?
"""
# Created an empty list
created_list = []
print("Id of empty list: %s" % id(created_list))

# Append name to created list
created_list.append("Ram")
created_list.append("Hari")
created_list.append("Shyam")
created_list.append("Raju")

print("list with name of friends \n %s" % created_list)
print("Id of list after appending friends name : %s" % id(created_list))
# Id of the list didn't change.
sorted_list = sorted(created_list)
print("Sorted list \n %s" % sorted_list)
# Id of the list did't change even after sorting
print("Id of sorted of sorted list : %s" % id(sorted_list))
# first item of the list
print(sorted_list[0])
# second item of the list
print(sorted_list[1])
