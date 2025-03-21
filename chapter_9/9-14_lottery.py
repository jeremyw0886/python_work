# 9-14_lottery.py
import random

# List of 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

# Randomly select 4 numbers and 1 letter
numbers = [x for x in lottery_pool if isinstance(x, int)]
letters = [x for x in lottery_pool if isinstance(x, str)]
winning_numbers = random.sample(numbers, 4)
winning_letter = random.choice(letters)
winning_ticket = winning_numbers + [winning_letter]

# Get user input
print("Enter your lottery ticket (4 numbers and 1 letter).")
print("Examples: '1 2 3 4 A' or '1234A' (spaces optional)")
user_input = input("Your ticket: ").replace(" ", "")  # Remove all spaces

# Parse input
try:
    if len(user_input) != 5:
        raise ValueError("Invalid length! Must be 4 numbers and 1 letter.")
    user_numbers = [int(user_input[i]) for i in range(4)]
    user_letter = user_input[4].upper()
    user_ticket = user_numbers + [user_letter]
except ValueError as e:
    print(f"Error: {e}")
    print("Please restart and enter a valid ticket.")
    exit()

# Compare tickets
print(f"\nWinning ticket: {winning_ticket}")
print(f"Your ticket: {user_ticket}")
if user_ticket == winning_ticket:
    print("Congratulations! You're a winner!")
else:
    print("Sorry, you didn't win this time.")
