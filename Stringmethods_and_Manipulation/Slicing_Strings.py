'''
Write a Python program to slice the string "Programming" to obtain:
"Pro"
"gramming"
"ogramm"
'''
string = "Programming"
slice1 = string[0:3]
slice2 = string[3:11]
slice3 = string[2:8]
print(f"First Pattern: {slice1}")
print(f"Second Pattern: {slice2}")
print(f"Third Pattern: {slice3}")



'''
If s = "Data Science", write code to:
Extract "Data"
Extract "Science"
Reverse the string using slicing.
'''
s = "Data Science"
extract1 = s[0:4]
extract2 = s[5:13]
print(f"extract 1: {extract1}")
print(f"extract 2: {extract2}")
print(f"Reversed string is: {s[::-1]}")


'''
Write a program to input a string from the user and print:
The first half of the string.
The last three characters.
'''
inp_str = input("Enter the string: ")
frst_half = inp_str[:len(inp_str) // 2]
lst_three = inp_str[-3:]
print(f"The first half of the string: {frst_half}")
print(f"The last three characters: {lst_three}")


'''
Given quote = "Python is fun", use slicing to:
Print "fun".
Remove the last word.
Print every alternate character.
'''
quote = "Python is fun"
frst_wrd = quote[10:13]
without_last_word = quote[:quote.rfind(" ")]
print(frst_wrd)
print(f"Last word removed: {without_last_word}")
print(f"Alternate characters: {quote[::-1]}")


'''
Write a program that takes a string and a step value (e.g., 2) from the user, and prints every second character using slicing.
'''
inp_txt = str(input("Enter the string: "))
inp_val = int(input("Enter the value to be sliced: "))
altr_str = inp_txt[::(inp_val)]
print(f"The altered string is: {altr_str}")