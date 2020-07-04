"""
Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case
(i.e.this_is_camel_cased). Modify the function by adding an argument,separator,
so it will also convert to the kebab case (i.e.this-is-camel-case) as well.
"""


def snakeCase(input_string):
    res = [input_string[0].lower()]
    for c in input_string[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
    return ''.join(res)


def kebabCase(input_string, separator):
    word = snakeCase(input_string)
    print(word.replace('_', separator))


str = "ThisIsCamelCased"
print(snakeCase(str))
kebabCase(str, '-')
