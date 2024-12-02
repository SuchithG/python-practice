# Example program for string manipulation , ip/op statements and types of comments

# Define input fields
boy_name = input("Enter boy name: ")
boy_age = int(input("Boy age: "))
girl_name = input("Enter girl name: ")
girl_age = int(input("Girl age: "))

'''
Age Difference
Using abs to maintain positive age 
'''
age_diff = abs(boy_age - girl_age)

print(boy_name + " loves " +  girl_name + " Their age difference is: " + str(age_diff))

print(f"{boy_name} loves {girl_name} their age difference is {age_diff}")  # formatted string
