# Basic example
for i in range(1, 11):
    print(i, end=" ")

# Using step inside range
for j in range(1,20, 2):
    print(j, end=" ")

# looping over staring using enumerate
l = "suchith"

for index , alp in enumerate(l):
    print(alp*(index+1))


num_list = [1, 12, 13, 14, 15, 16, 17, 18, 19]

for i, num in enumerate(num_list):
    print(f"The number {num} is in the {i}th index1")
    print(num*i+1)