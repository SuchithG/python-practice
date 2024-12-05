'''
Write a Python program that performs basic arithmetic operations (addition, subtraction, multiplication and 
division) on two numbers. Define the two numbers as variables within the code and print the results for each operation.
'''

a = 2 
b = 3

print("Addition",a + b) # 5
print("Subtraction", a - b) # 1
print("Multiplication", a * b) # 6
print("Division", a / b) # 0.666...
print("Floor division", a // b) # 0  (Floor division)
print("Modulus/Remainder", a % b) # 0.66 (Modulus|Remainder)
print("Exponentiation", a ** b) # Exponentiation/Power



# BODMAS
print(a+b+(a-b)*a-(b-a)/b) 

# write a program to swap two numbers
a = 2
b = 3
a , b = b, a
print(a)
print(b)