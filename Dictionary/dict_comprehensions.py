# Dictionary Comprehension
#Similar to list comprehension, dictionary comprehension provides a concise way to create dictionaries. 

# Syntax : new_dict = {key_expression: value_expression for item in iterable if condition}

numbers = [1, 2, 3, 4, 5]
squares = {num: num*num for num in numbers}
print(squares)

# eg: 2
names = ['adam', 'biran', 'casper']
d = {name:len(name) for name in names}
print(d)