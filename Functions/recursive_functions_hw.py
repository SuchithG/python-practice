# Example 1:
# Write a recursive function that calculates the sum of the first n numbers.

def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)

print(sum_of_numbers(3))

# Example 2:
# Write a recursive function to calculate the factorial of a number n

def factorial_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n * factorial_of_numbers(n - 1)
    
print(factorial_of_numbers(3))

# Example 3:
# Write a recursive function to find the n-th Fibonacci number
def fib_of_numbers(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_of_numbers(n - 1) + fib_of_numbers(n - 2)

print( fib_of_numbers(3))( fib_of_numbers(3))


