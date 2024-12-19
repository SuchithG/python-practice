#List Manipulation:

#Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

kannada_foods = ["uppitu", "bisibelebath", "palav", "idli", "dose", "chithranna"]

uppercase_food_names = [ up_fd_nme.upper() for up_fd_nme in kannada_foods]
print(uppercase_food_names)

#Sum of Prices:
#Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.

items_prices = {
    "items_1": 5,
    "items_2": 6,
    "items_3": 7,
    "items_4": 8,
    "items_5": 10,
}
sum_prices = 0

for value in items_prices.values():
    sum_prices += value
    
print(sum_prices)

#List of Squares:
#Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.

squares = [ num**2 for num in range(1, 11)]
print(squares)


#Student Data Task:
#Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. 
# Loop through the list and print each student's information.

students = [
    {
        "name": "student_1",
        "age": 23,
        "marks": 25
    },
    {
        "name": "student_2",
        "age": 24,
        "marks": 27
    },
    {
        "name": "student_3",
        "age": 25,
        "marks": 30
    },
]

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

#Dictionary Comprehension:

# Create a dictionary where the keys are Kannada cities, and the values are their populations. 
# Use dictionary comprehension to filter out cities with populations below 10 lakhs.

city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}

small_cities = {city:population for city, population in city_population.items() if population >= 10}
print(small_cities)

'''
Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

- Prints the entire matrix row by row.
- Prints the sum of each row in the matrix.
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i,j in enumerate(matrix):
    print(f"{i}.The sum of the list {j} is : {sum(j)}")