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