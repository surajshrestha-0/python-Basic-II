"""
Write a binary search function. It should take a sorted sequence and the item it is looking for.
It should return the index of the item if found. It should return -1 if the item is not found.
"""


def binarySearch(sequence, item):
    sequence = sorted(sequence)
    low = 0
    high = len(sequence) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        # Check if item is present at mid
        if sequence[mid] < item:
            low = mid + 1
        # If item is greater, ignore left half
        elif sequence[mid] > item:
            high = mid - 1
        # If item is smaller, ignore right half
        else:
            return 'Index of the item : %d' % mid
        # If we reach here, then the element was not present
    return -1


number_sequence = [2, 3, 4, 10, 40]
x = 12
y = 4

# Function call
print(binarySearch(number_sequence, x))
print(binarySearch(number_sequence, y))
