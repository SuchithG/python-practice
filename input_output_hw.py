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


# Ask the user for a number and print its multiplication table up to 10.
number = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{number} x {i} = {number * i}")


# Ask the user for two numbers and an operation (add, subtract, multiply, divide). Perform the operation and display the result.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

# Perform the calculation based on the operation
if operation == "add":
    result = num1 + num2
    print(f"The result is {result}.")
elif operation == "subtract":
    result = num1 - num2
    print(f"The result is {result}.")
elif operation == "multiply":
    result = num1 * num2
    print(f"The result is {result}.")
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is {result}.")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
