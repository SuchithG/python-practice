# Lambda Function: 
# Example: Write a lambda function that multiplies two numbers.

mul = lambda a, b: a * b
result = mul(2,3)
print(result)

# Basic Arithmetic with Lambda
# Example 1: Write a lambda function to add two numbers.
add = lambda x,y: x + y
result = add(9,10)
print(result)

# Example 2: Write a lambda function to subtract two numbers.
sub = lambda x,y: x - y
result = abs(sub(9,10))
print(result)

# Example 3: Write a lambda function to divide one number by another and handle division by zero
div = lambda x,y: "Division by zero is not allowed" if y==0 else x // y
print((div(10,2)))
print((div(10,0)))

# String Manipulation
# Example 1: Create a lambda function that takes a string and returns its uppercase version.
s = str(input("Enter a work or a string: "))
upp_str = lambda s: s.upper()
print(upp_str(s))

# Example 2: Write a lambda function that checks if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]
input_string = input("Enter a word: ").upper().strip()
if is_palindrome(input_string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# Example 3: Create a lambda function that returns the length of a string

v = str(input("Enter the string"))

len_v = lambda v: len(v)
print(len_v(v))


# Working with Lists
# Example 1: Write a lambda function to square all elements in a list using map().
square = list(map(lambda x: x**2, range(1, 6)))
print(square)

# Example 2: Create a lambda function to filter out all even numbers from a list using filter().
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 6)))
print(even_numbers)

# Example 3: Use a lambda function to sort a list of tuples based on the second element of each tuple
a = [(1, 'cherry'), (2, 'apple'), (3, 'banana'), ]
sorted_list = sorted(a, key=lambda x: x[0])
print(sorted_list)


# Boolean Logic
# Example 1: Write a lambda function to check if a number is positive, negative, or zero.
x = int(input("Enter a number: "))

num_check = "positive" if x>0 else "negative" if x<0 else "zero"
print(num_check)

# Example 2:
# Write a lambda function to check if a number is divisible by both 3 and 5
n = int(input("Enter a number to check if it's divisible by 3 and 5: "))
check = "The number is divisible by 3 and 5" if n % 3 == 0 and n % 5 == 0 else "The number is not divisible by 3 and 5"
print(check)

# Example 3:
# Create a lambda function that returns True if a given year is a leap year and False otherwise
year = int(input("Enter a year in 4 digits: "))

leap_year = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(leap_year(2024)) # True
print(leap_year(1900)) # False
print(leap_year(2000)) # True