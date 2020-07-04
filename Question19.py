"""
Write a Python class to find validity of a string of parentheses, '(',')', '{', '}', '[' and '].
These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
"""


class ValidatedParentheses:
    def orderCheck(self, input_string):
        open_tup = tuple('({[')
        close_tup = tuple(')}]')
        map = dict(zip(open_tup, close_tup))
        queue = []
        for i in input_string:
            if i in open_tup:
                queue.append(map[i])
            elif i in close_tup:
                if not queue or i != queue.pop():
                    return "Invalid"
        if not queue:
            return "Valid"
        else:
            return "Invalid"


print(ValidatedParentheses().orderCheck("()"))
print(ValidatedParentheses().orderCheck("()[]{}"))
print(ValidatedParentheses().orderCheck("({[)]"))
print(ValidatedParentheses().orderCheck("{{{"))
