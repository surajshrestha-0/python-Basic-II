"""
Write a Python class to find the three elements that sum to zero from a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""


def sumThreeElements(input_number):
    input_number = sorted(input_number)
    output_result = []
    length = 0
    while length < len(input_number) - 2:
        i = length + 1
        j = len(input_number) - 1
        while i < j:
            if input_number[length] + input_number[i] + input_number[j] < 0:
                i += 1
            elif input_number[length] + input_number[i] + input_number[j] > 0:
                j -= 1
            else:
                output_result.append([input_number[length], input_number[i], input_number[j]])
                i, j = i + 1, j - 1
                while i < j and input_number[i] == input_number[i - 1]:
                    i += 1
                while i < j and input_number[j] == input_number[j + 1]:
                    j -= 1
        length += 1
        while length < len(input_number) - 2 and input_number[length] == input_number[length - 1]:
            length += 1
    return output_result


print(sumThreeElements([-25, -10, -7, -3, 2, 4, 8, 10]))
