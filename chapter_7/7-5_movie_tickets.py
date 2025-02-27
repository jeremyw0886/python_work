# Ask users for their age in a loop
# Determine ticket price based on age ranges
# Exit when they enter 'quit'
while True:
    age = input("Enter your age (or 'quit' to finish): ")
    if age == 'quit':
        break
    # Convert age to integer
    age = int(age)

    # Determine ticket price
    if age < 3:
        print("Your ticket is free.")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
