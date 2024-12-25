# Example 1:
# Write a recursive function that calculates the sum of the first n numbers.

def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)

print(sum_of_numbers(3))