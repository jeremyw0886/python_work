# Define a tuple with five simple foods
foods = ('pizza', 'burger', 'pasta', 'salad', 'soup')

# Use a for loop to print each food the restaurant offers
print("Original menu:")
for food in foods:
  print(food)

# Try to modify one of the items (this should raise an error)
try:
  foods[0] = 'sushi'
except TypeError as e:
  print(f"\nError: {e}")

# The restaurant changes its menu, replacing two of the items with different foods
foods = ('sushi', 'burger', 'pasta', 'steak', 'soup')

# Use a for loop to print each of the items on the revised menu
print("\nRevised menu:")
for food in foods:
  print(food)
