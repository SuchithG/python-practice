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