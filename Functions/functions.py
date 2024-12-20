# Functions
# Basic synatx
def function_name(parameters):
    # Block of code
    print("")


# Basic function to greet a user
def greet():
     print("Hello users!")
greet()

# Function Parameters
# Function with a parameter
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course.")

greet_user("Anand")

# Ex: 1    
def marriage(boy, girl): #parameters
    print(f"{boy} married {girl}")

marriage("John", "Selina") #positional parameters

marriage(boy="Johnny", girl="clay") #keyword parameters

# Default Parameter Values
# Function with a default parameter
# Ex: 1
def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the Python course.")

greet()  # Uses default value "Student"
greet("Geetha")  # Uses passed value "Geetha"

# Ex: 2
def tables(num=4): # Default parameters values
    for i in range(1,11):
            print(f"{num} X {i} = {num*i}")


tables()


# Returning Values from a Function
# Function that adds two numbers and returns the result

def add_numbers(a, b):
     return a + b

result = add_numbers(2, 3)
print("The sum is", result)