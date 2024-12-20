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


# Ex: 2
def tables(num):
    for i in range(1,11):
            print(f"{num} X {i} = {num*i}")


tables(1)