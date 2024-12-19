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
