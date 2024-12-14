# Basic example
for i in range(1, 11):
    print(i, end=" ")

# Using step inside range
for j in range(1,20, 2):
    print(j, end=" ")

# looping over staring using enumerate
l = "suchith"

for index , alp in enumerate(l):
    print(alp*(index+1))


num_list = [1, 12, 13, 14, 15, 16, 17, 18, 19]

for i, num in enumerate(num_list):
    print(f"The number {num} is in the {i}th index1")
    print(num*i+1)

# Nested for loops
# Let’s print the multiplication table from 1 to 5 using a nested for loop.

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()

# Using break in for loop
# Stop the loop when you find a specific item
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
for city in cities:
    if city == "Hubballi":
        print(f"found {city}!")
        break
    else:
        continue
print(city)

# Using "continue" in a for loop
# Let’s skip "Hubballi" while looping through the cities:

for city in cities:
    if city == "Hubballi":
        continue
    print(city)

# Looping through the list with enumerate
#Displaying the index and value of each city
cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]

for index, city in enumerate(cities):
    print(f"City {index+1}: {city}") 


# using else with for loop

for index, city in enumerate(cities):
    print(city)
else:
    print("No more cities!")