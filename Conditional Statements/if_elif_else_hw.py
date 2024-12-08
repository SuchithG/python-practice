'''
Basic Conditions:

- Write a program to check if someone is eligible for a bus pass. 
If they are below 5 years, the bus pass is free. 
If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.
'''

age = int(input("Enter your age: "))

if age < 5:
    print("Bus pass is free!")
elif age >= 60:
    print("Free senior citizen discount!")
else:
    print("Please pay the full price")

'''
Meal Time Checker:

- Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
- Breakfast: 8 AM
- Lunch: 1 PM
- Dinner: 8 PM
- If none of these times, print "It's not meal time."
'''
try:
    time = int(input("Enter your time in (24-hour format, 0-23): " ))

    if 0 <= time <=23:
        if time == 8:
            print("Its time for breakfast!")
        elif time == 13:
            print("Its time for lunch!")
        elif time == 20:
            print("Its time for Dinner!")
        else:
            print("It's not meal time.")
    else:
        print("Invalid time! Please enter a number between 0 and 23.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

'''
Simple Eligibility Check:
Write a program that checks whether a person is eligible for a library membership. 
If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership.
Otherwise, they get a regular membership.
'''

age = int(input("Enter your age in years: "))

if 0 <= age <= 65:
    if age <= 18:
        print("Congratulations! You are eligible for a student membership")
    elif age >= 60:
        print("Congratulations! You are eligible for a senior citizen membership")
    else:
        print("You get a regular membership")
else:
    print("Oops ! you are not eligible for a library membership")
