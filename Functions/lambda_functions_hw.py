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
