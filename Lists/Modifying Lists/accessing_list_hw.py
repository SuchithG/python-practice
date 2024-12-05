# Basic access 
'''
Create a list fruits = ["apple", "banana", "cherry", "date", "elderberry"]. Access and print:

-The first element.
-The last element.
-The third element.
'''

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"The first element is {fruits[0]}") # The first element.
print(f"The last element is {fruits[-1]}") # The last element.
print(f"The third element is {fruits[4]}") # The third element.

'''
Given the list numbers = [10, 20, 30, 40, 50]:

- Access and print the second element.
- Access and print the element at index -2.
'''

list_numbers = [10, 20, 30, 40, 50]

second_element = list_numbers[3]
print(f"The second element is: {second_element}")
index2 = list_numbers[-2]
print(f"The element at index -2 is: {index2} ")

# Slicing

'''
Using the list letters = ["a", "b", "c", "d", "e", "f"]:

-Slice and print the first three elements.
-Slice and print the last three elements.
-Slice and print all elements except the first two.
'''

list_letters = ["a", "b", "c", "d", "e", "f"]
slice_first_3 = list_letters[:3]
print(f"The first three elements are: {slice_first_3}")
slice_last_3 = list_letters[-3:]
print(f"The first three elements are: {slice_last_3}")
except_first_2 = list_letters[2:]
print(f"All elements except the first two: {except_first_2}")

# Reverse the list letters using slicing and print it.
reversed_list = list_letters[::-1]
#list_letters.reverse()
print(f"Reversed list id: {reversed_list}")

# Modifying and Accessing Nested Lists
'''
Given the nested list matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
Access the element 5.
Print the second row ([4, 5, 6]).
Replace the element 9 with 0 and print the updated list.
'''

matrix = [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]
        ]

print(matrix[1][1])
print(matrix[1])
matrix[2][2] = 0
#updated_list1 = updated_list.append(1)
print(f"Updated list : {matrix}")


