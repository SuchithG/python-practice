# Write a Python program to extract the first and last characters of the string "Programming"
word = "Programming"
first_char = word[0]
last_char = word[-1]
print(f"First and last characters of the word are: {first_char} and {last_char}")

# Given a string "Hello, World!", access and print the 7th character from the string.
string = "Hello, World!"
seventh_char = string[7]
print(f"The 7th character from the string is: {seventh_char}")

"""
If s = "Python", how would you access:
The second character?
The last character?
"""
s = "Python"
second_char = s[1]
last_chart = s[-1]
print(f"The second character and the last character are: {second_char} and {last_chart}")

# Write a program to input a string from the user and print the character at index 3 (if it exists).
input_string = str(input("Enter your string: "))
indx_str = input_string[2]
print(f"Character at index 3 is: {indx_str}")

# Given a string word = "developer", write a program to check if the third character is a vowel.
word = "developer"
third_char = word[2]

if third_char in "aeiouAEIOU":
    print(f"The third character {third_char} is a vowel.")
else:
    print(f"The third character {third_char} is not a vowel.")