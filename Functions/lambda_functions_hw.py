'''
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
div = lambda x,y: "Divison by zero is not allowed" if y==0 else x // y
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
'''

# Working with Lists
# Example 1: Write a lambda function to square all elements in a list using map().

square = list(map(lambda x: x**2, range(1, 6)))
print(square)

# Example 2: Create a lambda function to filter out all even numbers from a list using filter().

even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 6)))
print(even_numbers)

