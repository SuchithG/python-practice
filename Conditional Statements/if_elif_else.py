# Let’s create a system to check meal times based on the time of the day
# if statement, else, elif statement
time = int(input(f"Enter the time hrs in 24hr format (eg: 16) : "))

if time == 8:
    print("It's breakfast time!")
elif time == 13:
    print("It's lunch time!")
elif time == 20:
    print("It's dinner time!")
else:
    print("It's not a meal time.")

#Comparison Operators in if Statements
# example 1
age = 19

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# example 2
age = 16
has_student_id = True

if age < 18 and has_student_id:
    print("You are eligible for the student discount!")
else:
    print("You are not eligible for the student discount.")

# Nested if Statements

# Let’s say you’re planning to visit Mysuru. You want to decide whether to go based on the day of the week and the weather.
day = "Saturday"
is_raining = False

if day == "Saturday" or day == "Sunday":
    if not is_raining:
        print("Let's visit Mysuru!")
    else:
        print("It's raining, let's stay home.")
else:
    print("It's a weekday, let's wait for the weekend.")