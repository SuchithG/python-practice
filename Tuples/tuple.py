# Tuple indexing
fruits = ["apple", "banana", "cherry", "pineapple", "peach", "plum"]

print(fruits[1]) # Output: "banana"
print(fruits[-1]) # Output: "plum"

# Slicing Tuples
print(fruits[0:3]) # Output: 'apple', 'banana', 'cherry'

# Tuple Operations
# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple) # Output: (1, 2, 3, 4, 5, 6)

# Tuple Repetition
repeated_tuple = (1,2) * 3
print(repeated_tuple) # Output: (1, 2, 1, 2, 1, 2)

#Checking Membership
print("apple" in fruits) # Output: True


# Tuple Methods

my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))  # Output: 3

my_tuple1 = ("apple", "banana", "cherry")
print(my_tuple1.index("cherry")) # Output: 1
