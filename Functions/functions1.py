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

# Example2: 
def tot_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
        return result
    
print(total_sum(8, 9, 10))

# Using **kwargs
# Example: 
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")

# Lambda Functions
# Syntax: lambda arguments: expression

double = lambda x: x * 2
print(double(5))

# Example2:

students = [
    {'name': 'Student1', 'marks': 30},
    {'name': 'Student2', 'marks': 90},
    {'name': 'Student3', 'marks': 70}
]

students.sort(key= lambda x: x["marks"], reverse=True)
print(students)

# Recursion
# Recursion occurs when a function calls itself. It's used to solve problems that can be broken down into smaller, similar problems.
# Example: Recursive function to calculate factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
        
