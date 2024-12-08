# Creating a dictionary
# Syntax
# You can create a dictionary using curly braces {} or the dict() function
my_dict = {
    "key1": "value1", # Key value pairs
    "key2": "value2",
    "key3": "value3"
}

my_dict1 = {
    "key1": "value1", # Key value pairs
    "key2": "value2",
    "key3": "value3",
    123: 123
}

print(my_dict1)

# using the dict() function
new_dict = dict(Suchith="Male", Shashank="Male")
print(new_dict)

# Example 2 : Let's create a dictionary of famous cities in Karnataka and their popular dishes
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}

# Accessing the dictionary
print(karnataka_food["Mysuru"])

# using get() method
print(new_dict.get("Suchith","Shashank"))

# Adding and updating the dictionary elements
# Adding to list
my_dict["key4"] = "value4"
print(f"Updated list in my_dict: {my_dict}")

# Updating the existing 
karnataka_food["Bengaluru"] = "Ragi Ball"
print(f"Updated karnataka_food: {karnataka_food}")

# Removing from dict
karnataka_food.pop("Mangaluru")
print(f"Removed from dict: {karnataka_food}")

# Removing using del keyword
del my_dict["key4"]
print(f"Removed from dict: {my_dict}")

# Removing using clear
my_dict1.clear()


# Dictionary Methods
# Keys
print(new_dict.keys())

# Value
print(new_dict.values())

# items
print(new_dict.items())

# Update 
updated_dict = {"suchitha":"Female"}
new_dict.update(updated_dict)
print(f"The updated new_dict is: {new_dict}")
