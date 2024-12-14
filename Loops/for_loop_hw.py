'''
Multiples of 3:

- Write a for loop that prints all multiples of 3 between 1 and 30.
'''

for i in range(1, 31):
    print(f"3 X {i} = {3*i}")


'''
Sum of First 10 Numbers:

- Write a program using a for loop that calculates the sum of numbers from 1 to 10.
'''
sum_of_numbers = 0
for i in range(1, 11):
    sum_of_numbers += i
print(sum_of_numbers)

'''
Print Your Name Letter by Letter:

- Write a program that takes your name as input and prints each letter of your name using a for loop.
'''
name = input("Enter your name: ")

for i, j in enumerate(name):
    print(f"The letter in first poition - {i+1} is : {j}")

'''
Count Vowels in a String:

- Write a program that counts how many vowels are in a given string using a for loop.
'''

vowels = ["a", "e", "i", "o", "u"]

string =  str(input("Enter the string: ").lower())

count = 0

for i in string:
    if i in vowels:
        print(f"Found an vowel in the string: {i}")
        count += 1
    else:
        continue
print(f"Total no of vowels found is : {count}")