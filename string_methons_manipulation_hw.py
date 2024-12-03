'''
Simple Greeting Program: Write a Python program that asks the user for their name and age, 
then prints a personalized greeting message. 
Use both the + operator and f-strings for output.
'''
user_name = str(input("Enter your name: "))
user_age = int(input("Enter your age: "))
print("Hello, " + user_name + "! You are " + str(user_age) + " years old.") # using +
print(f"Hello, {user_name}! You are {user_age} years old.") # using f-strings

'''
String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
'''
user_input = input("Enter your name: ")
Uppercase = user_input.upper().strip()
Lowercase = user_input.lower()
remove_space_with_underscore = user_input.replace(" ", "_")
remove_leading_and_trailing_whitespace = user_input.strip()
print(f"Uppercase: {Uppercase}!")
print(f"Lowercase: {Lowercase}")
print(f"Space replaced with underscores: {remove_space_with_underscore}")
print(f"Removes leading and trailing whitespaces: {remove_leading_and_trailing_whitespace}!") # lstrip() or rstrip()


'''
Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces.
'''
input_string = (str(input("Enter your name: "))).replace(" ", "")
altered_string = len(input_string)
print(f"Number of characters (excluding spaces): {altered_string}")


'''
Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:
'''
print("Hello\n    World\nThis is a backslash: \\")
