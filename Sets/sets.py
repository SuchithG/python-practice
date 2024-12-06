#------Declaring a set-------#
s = {1,2,3,4,5,6,7,8,9} # using "{ }"

s1 = set((1,2,3)) # using set function 
#s1 = set([(1,2,3),("Python",),(3,)])  # The set() function expects a single iterable, like a list, tuple, or string, from which it will construct the set.

# Declaring empty set
s2 = set()

print(type(s2))


#-----Set Operations------#
# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2) # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1 & set2
print(intersection_set) # Output: {3}

# Difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A - B  # Elements in A but not in B
print(result)

# Symmetric Difference ( ^ )
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A ^ B  # Elements in A or B, but not both
print(result)
