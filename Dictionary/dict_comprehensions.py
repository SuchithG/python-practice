# Dictionary Comprehension
#Similar to list comprehension, dictionary comprehension provides a concise way to create dictionaries. 

# Syntax : new_dict = {key_expression: value_expression for item in iterable if condition}

numbers = [1, 2, 3, 4, 5]
squares = {num: num*num for num in numbers}
print(squares)

# eg: Converting a list of names to a dictionary of name lengths
names = ['adam', 'biran', 'casper']
d = {name:len(name) for name in names}
print(d)

#Filtering cities with population above 10 lakhs (Localized Example)

city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}

large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)