# List comprehension provides a more concise way to create lists by applying an expression to each element in an existing list
# Syntax : new_list = [expression for item in iterable if condition]

# eg: Squaring numbers in a list
numbers = [1, 2, 3, 4, 5, 6]
squares = [num*2 for num in numbers]
print(squares)

# eg: Filtering even numbers
even_numbers = [num for num in numbers if num%2 == 0 ]
print(even_numbers)

# eg: Uppercasing Kannada city names
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
uppercase_cities = [c.upper() for c in cities]
print(uppercase_cities)