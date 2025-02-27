# Ask the user for a number
# Check if it’s a multiple of 10 using the modulo operator
# Report the result to the user
number = int(input("Please enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
