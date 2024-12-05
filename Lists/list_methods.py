fruits = ["apple", "banana", "orange", "mango", "kiwi", "jackfruit", "jackfruit"]
num = [1, 2, 7, 4, 5, 6, 3, 8]

print(fruits.index("apple")) # Returns the index of the first occurrence of the specified element

print(fruits.count("jackfruit")) # Returns the number of occurrences of an element in the list

num.sort()
num.reverse()
print(num)

# Accessing elements in a nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])