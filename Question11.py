"""
Create a variable, filename.
Assuming that it has a three-letter extension, and using slice operations, find the extension.
For README.txt, the extension should be txt. Write code using slice operations that will
give the name without the extension.
Does your code work on filenames of arbitrary length?
"""
import os

# created a variable filename
filename = "file.pdf"
# Assuming that it has a three-letter extension , and using slice operations
file_extenstion = filename[-3:]
# printing file extension
print(file_extenstion)

nameWithExtension = 'README.txt'
# slicing using os path. so, that code work on filenames of arbitrary length
filename = os.path.splitext(nameWithExtension)[0]
print(filename)
