'''
Basic Counting with while Loop:

- Write a program that counts from 1 to 10 using a while loop.
'''
number = 1

while number<=10:
    print(f"The count of numbers is: {number}")
    number += 1

'''
Odd Numbers Printer:

- Create a program that prints all odd numbers between 1 and 20 using a while loop.
'''

num = 1

while num <= 20:
    if num % 2 != 0:
        print(f"The number is {num}")
    num += 1

'''
Ticket Booking Simulation:

- Write a program that simulates a bus ticket booking system. 
- The bus has 8 seats. Each time a seat is booked, the available seats decrease. 
- When there are no seats left, the loop stops and displays a message saying "All seats are booked."
'''

available_seats = 8

while available_seats > 0:
    print(f"{available_seats} seats available")
    booking = input(f"Do you want to book a ticket? (y/n): ").lower()

    if booking == 'y':
        available_seats -= 1
        print("Seat booked")
    else:
        print("No booking available")
print("All seats are booked!")

'''
Countdown Timer:

- Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.
'''

count_down = 10

while count_down > 0:
    print(f"Countdown in: {count_down} seconds")
    count_down -= 1

print("Happy New Year!")