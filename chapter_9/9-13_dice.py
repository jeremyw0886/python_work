# 9-13_dice.py
from random import randint


class Die:
    """A simple model of a die."""

    def __init__(self, sides=6):
        """Initialize die with a number of sides."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        roll = randint(1, self.sides)
        print(roll)


# Create a 6-sided die and roll it 10 times
print("Rolling a 6-sided die 10 times:")
die_6 = Die()  # Default is 6 sides
for _ in range(10):
    die_6.roll_die()

# Create a 10-sided die and roll it 10 times
print("\nRolling a 10-sided die 10 times:")
die_10 = Die(10)
for _ in range(10):
    die_10.roll_die()

# Create a 20-sided die and roll it 10 times
print("\nRolling a 20-sided die 10 times:")
die_20 = Die(20)
for _ in range(10):
    die_20.roll_die()
