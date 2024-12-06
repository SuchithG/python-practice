"""
Set Operations:

- Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
- Find the union, intersection, and difference between the two sets.
- Add a new fruit to your set.
- Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
"""

fruits1 = {"apple", "orange", "mango"}
fruits2 = {"orange", "banana", "apple"}
print(f"Union: {fruits1 | fruits2}") 
print(f"Intersection: {fruits1 & fruits2}")
print(f"Difference: {fruits1 - fruits2}")
fruits1.add("grapes")
print(f"My updated fruits set is: {fruits1}")
fruits1.remove("apple")
print(f"My updated fruits list is: {fruits1}")
fruits1.discard("apple")
print(f"My updated fruits list is: {fruits1}") # No error if the fruit does not exist in the list

"""
Tuple and Set Comparison:

- Create a list of elements and convert it into both a tuple and a set.
- Print both the tuple and the set.
- Try to add new elements to the tuple and set. What differences do you observe?
"""

l = ["one", "two", "three", "four", "five", "six"]
l_tuple = tuple(l)
print(f"List converted into tuple: {l_tuple}")
l_set = set(l)
print(f"List converted into set: {l_set}")
#l_tuple.add("one") Python will raise an AttributeError, as tuples do not support methods like add() or append().
#print(l_tuple) Output: Error: 'tuple' object has no attribute 'add'
l_set.add("one")
print(l_set)

