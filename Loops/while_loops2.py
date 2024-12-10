# left pyramid 
i = 0

while i<=10:
    x = 0
    while x<i:
        print("Suchith", end="-")
        x += 1
    print("")
    i += 1

# Let’s say you want to simulate a KSRTC bus seat booking system. 
# The bus has 5 available seats. 
# Each time a seat is booked, the available seats decrease.
available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats -= 1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")

# Nested while loops
# Let’s simulate a snack machine that allows users to buy snacks as long as both the machine has snacks and the user has money:

snacks_available = 3
money = 10

while snacks_available > 0 and money > 0:
    print(f"Snacks available: {snacks_available}. Money: {money}")
    buy = input("Do you want to buy a snack for Rs 5? (yes/no): ").lower()

    if buy == "yes" and money >= 5:
        snacks_available -= 1
        money -= 5
        print("Snacks purchased!")
    else:
        print("No purchase made.")

print("Either snacks are sold out or you are out of money!")