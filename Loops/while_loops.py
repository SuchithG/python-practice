# While loop

is_failed = True
i = 1

while is_failed:
    if i%2!=0:
           continue
    print(f"Try {i}")
    i = i + 1   
    if i > 100:
        break

# example 1: print numbers from 1 to 5 using a while loop

i = 1

while i <= 5:
    print(i)
    i += 1

# example 2: Imagine you're counting sheep to fall asleep

sheep_count = 1

while sheep_count <= 10:
    print(f"Sheet {sheep_count}")
    sheep_count += 1

i = 1
while i <= 5:
    print(i)
    i += 1

# example 3:

pin = "1234"

input_pin = int(input("PIN >> "))

if input_pin == pin:
     print("CORRECT PIN")
else:
     print("INCORRECT PIN")

# example 4:Let’s say you want to simulate a KSRTC bus seat booking system.
# The bus has 5 available seats. Each time a seat is booked, the available seats decrease.

available_sets = 5

while available_sets > 5:
    print(f"{available_sets} are available")
    booking = input("Do you want to book a seat? (yes/no): ").lower()

    if booking == "yes":
        available_sets -= 1
        print("Seats booked!")
    else:
        print("No booking made!")
print("All seats are booked!")


         
