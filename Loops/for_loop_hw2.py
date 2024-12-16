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


# Looping Through Dictionaries

# Iterating over dictionary keys
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(f"{student}")

# Iterating over dictionary values
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for marks in student_marks.values():
    print(marks)

# Iterating over both keys and values
student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student, marks in student_marks.items():
    print(f"{student} scored {marks} marks")

