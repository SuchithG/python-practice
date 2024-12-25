# Variable-Length Arguments
# Example 1
# Write a function that accepts any number of arguments and returns their average

def average(*n):
    return sum(n) / len(n)

print(f"{average(10, 30 , 28):.2f}")

