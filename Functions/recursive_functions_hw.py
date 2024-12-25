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

print( fib_of_numbers(3))

# Example 4:
# Write a recursive function to reverse a string
def reverse_string(string):
    # Base case: if the string is empty or has one character, it's already reversed
    if len(string) <= 1:
        return string
    else:
        # Recursive step: reverse the rest of the string and append the first character
        return reverse_string(string[1:]) + string[0]

# Example usage
print(reverse_string("Suchith"))

# Example 5:
# Write a recursive function to check if a given string is a palindrome (reads the same forward and backward).
def palindrome(string):
    # Base case: If the string has 0 or 1 character, it's a palindrome
    if len(string) <= 1:
        return True
    # Check if the first and last characters are the same
    if string[0] != string[-1]:
        return False
    # Recursive call on the middle part of the string
    return palindrome(string[1:-1])

# Example usage
print(palindrome("Suchith"))  # Output: False
print(palindrome("madam")) 

# Example 6:
# Sum of Digits
# Write a recursive function to calculate the sum of the digits of a given integer.
def sum_of_digits(n):
    # Base case: If the number is a single digit, return it
    if n < 10:
        return n
    # Recursive step: Add the last digit to the sum of the remaining digits
    return n % 10 + sum_of_digits(n // 10)

# Example usage
print(sum_of_digits(12345))  # Output: 15

