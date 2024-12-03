# Write a program that asks the user for their name and prints a greeting message.
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Write a program that takes two numbers as input from the user and prints their sum.
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
sum = num_1 + num_2
print(f"The sum is: {sum}")

#Ask the user for the radius of a circle and calculate its area.
radius = int(input("Enter the radius: "))
area = 3.14 * (radius * 2)
print(f"The area is {area} ")

# Ask the user to input a temperature in Celsius and convert it to Fahrenheit.
celsius = float(input("Enter the temperature: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is {fahrenheit:.1f}.")

# Write a program to take three numbers from the user and print the largest.
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
largest = max(num1, num2, num3)
print(f"The largest number is {largest}.")

# Take a string input from the user and print it reversed.
input_str = str(input("Enter the string to reverse: "))
output_str = input_str[::-1]
print(output_str)

# Ask the user for a string and print the number of characters in it.
input_str = str(input("Enter the input string: "))
print(f"The string has {len(input_str)} characters.")

# Take a sentence as input and print the number of words.
# Example 1:
input_str = (str(input("Enter the string: "))).split()
print(f"The sentence has {len(input_str)} words.")

# Example 2:
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())
print(f"The sentence has {word_count} words.")
