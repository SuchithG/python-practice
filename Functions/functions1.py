# Keyword arguments
# Example:

def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Kumar")

# Variable-Length arguments
# You can use *args and **kwargs to accept a variable number of arguments in a function.
# Example: Using *args

def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3, 4, 5))
