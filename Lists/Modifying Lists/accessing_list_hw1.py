'''
List Manipulation Exercise:

- Create a list of 5 items (strings or numbers).
- Add a new item to the end of the list and another at the second position.
- Remove the third item from the list.
- Print the list after each operation.
'''

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits.append("jackfruit")
print(fruits)
fruits.insert(1, "mango")
print(fruits)
fruits.remove("cherry")
print(fruits)

'''
Reverse and Sort a List: Create a list of numbers and:

- Sort it in descending order.
- Reverse the sorted list and print it.
'''

list_numbers = [1, 4, 3, 2, 7, 6, 5]
list_numbers.sort()
print(f"The sorted list is: {list_numbers}")
list_numbers.reverse()
print(f"List in descending order: {list_numbers}")
