#  Looping Through Lists

# Sum of all numbers in a list
numbers = [10, 20, 30, 40, 50]
total = 0

for i in numbers:
    total += i 

print(f"Total sum: {total}")


# Doubling each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Doubled sum:", doubled)


# Printing Kannada food items
foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")