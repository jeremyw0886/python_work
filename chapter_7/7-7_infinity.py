# Create an infinite loop that asks for ages and reports ticket prices
# This loop will never end on its own use CTRL + C to stop it
while True:
    age = int(input("Enter your age: "))
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
