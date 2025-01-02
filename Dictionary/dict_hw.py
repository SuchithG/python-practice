'''
Basic Dictionary Operations:

- Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
- Add a new city and its dish to the dictionary.
- Update the dish for Bengaluru.
- Remove one city from the dictionary.
- Use the keys() method to print all city names in the dictionary.
- Use the values() method to print all dishes in the dictionary.
'''
# Five cities with few of their famous dishes
karnataka_cities = {
    "Bangalore": ["Masala Dosa", "Ragi Mudde", "Bisi Bele Bath"],
    "Mysore": ["Mysore Pak", "Mysore Masala Dosa", "Chiroti"],
    "Mangalore": ["Neer Dosa", "Mangalore Buns", "Chicken Ghee Roast"],
    "Hubli-Dharwad": ["Girmit", "Dharwad Peda", "Jolad Roti"],
    "Udupi": ["Udupi Sambar", "Kotte Kadubu", "Goli Baje"],
 
}

# Adding a new city
karnataka_cities["Maddhur"] = "Maddur Vada" # add
print(karnataka_cities)

# Updating the dish for Bengaluru
karnataka_cities["Bangalore"] = ["Masala Dosa", "Ragi Mudde", "Bisi Bele Bath", "Kesari Bath"] # update
print(karnataka_cities)

# Removing a city
del karnataka_cities["Udupi"] # delete

#Use the keys() method to print all city names in the dictionary.
print(karnataka_cities.keys())

# Using the keys methods to print all city in the dictionary
print(f"The List of cities are: {karnataka_cities.keys()}")

# Using the values methods to print all city in the dictionary
print(f"The List of dishes are: {karnataka_cities.values()}")

# Using the values methods to print all city in the dictionary
all_dishes = []
for dishes in karnataka_cities.values():
    for dish in dishes:
        all_dishes.append(dish)

dishes_string = ", ".join(all_dishes)

print(f"The list of dish items are: {all_dishes}")

'''
Nested Dictionary Practice (Simple for now):

- Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
- Access and print the favorite food of one friend.
'''
# Dictionary with deatils of two friends
friends_details  = {
    "Friend1": {
        'name': 'suchith1',
        'favorite subject': 'maths',
        'favourite food': 'upit'
    },
    "Friend2":{
        'name': 'suchith2',
        'favorite subject': 'science',
        'favourite food': 'biryani'
    }
}

# print the favorite food of one friend
print(friends_details['Friend2']['favourite food'])








