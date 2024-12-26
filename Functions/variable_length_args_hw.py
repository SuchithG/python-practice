# Variable-Length Arguments
# Example 1
# Write a function that accepts any number of arguments and returns their average
def average(*n):
    return sum(n) / len(n)

print(f"{average(10, 30 , 28):.2f}")

# Example 2
# Sum of Squares
def Sum_of_Squares(*args):
    return sum(x**2 for x in args)

print(f"{Sum_of_Squares(1, 2, 3):.2f}")



