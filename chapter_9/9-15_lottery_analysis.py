# 9-15_lottery_analysis.py
import random

# List of 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

# Define my ticket
my_ticket = [2, 3, 5, 6, "B"]

# Counters for attempts
attempts = 0

# Loop until my_ticket wins
while True:
    # Randomly select 4 numbers and 1 letter
    numbers = [x for x in lottery_pool if isinstance(x, int)]
    letters = [x for x in lottery_pool if isinstance(x, str)]
    winning_numbers = random.sample(numbers, 4)
    winning_letter = random.choice(letters)
    winning_ticket = winning_numbers + [winning_letter]

    # Increment attempts
    attempts += 1

    # Check if my_ticket wins
    if my_ticket == winning_ticket:
        break

# Report results
print(f"My ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {attempts} attempts to win the lottery!")
