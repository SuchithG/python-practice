'''
Tuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.
'''

tup = (1, 2, 3, 4, 5)
tup1 = (1, 2, 3, 4, 6)
#tup[0] = 7 # 'tuple' object does not support item assignment
print(f"The second and third elements in this tuple are : {tup[1]} , {tup[2]}") 
concatenate = tup + tup1 
print(concatenate)