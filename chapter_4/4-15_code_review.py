# Using PEP 8 - revised 4-2_animals.py
print("\n" + "=" * 50)
print("4-2. ANIMALS.".center(50))
print("=" * 50 + "\n")

# List of different types of animals
animals = [
    'dog',
    'cat', 
    'bird'
]

# Loop through the list and print a message for each animal
for animal in animals:
    print(f"🐾 A {animal.title()} would make a great pet.")

# Print a final message
print("\n💝 Any of these animals would make a great pet!")
print("\n" + "=" * 50)

# Using PEP 8 - revised 4-11_my_pizza_your_pizza.py
print("\n" + "=" * 50)
print("4-11. MY PIZZA, YOUR PIZZA.".center(50))
print("=" * 50 + "\n")

# List of my favorite pizzas
my_pizzas = [
    'supreme',
    'caesar',
    'cheese'
]

# Make a copy of the list to represent my friend's favorite pizzas
friend_pizzas = my_pizzas[:]

# Add a new pizza to my list
my_pizzas.append('pepperoni')

# Add a different new pizza to my friend's list
friend_pizzas.append('margherita')

# Print my favorite pizzas
print("🍕 My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"  • {pizza.title()}")

# Print my friend's favorite pizzas
print("\n🍕 My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"  • {pizza.title()}")
print("\n" + "=" * 50)

# Using PEP 8 - revised 4-13_buffet.py
print("\n" + "=" * 50)
print("4-13. BUFFET.".center(50))
print("=" * 50 + "\n")

# Define a tuple with five simple foods
foods = (
    'pizza',
    'burger',
    'pasta',
    'salad',
    'soup'
)

# Use a for loop to print each food the restaurant offers
print("📋 Original Menu:")
for food in foods:
    print(f"  • {food.title()}")

# Try to modify one of the items (this should raise an error)
try:
    foods[0] = 'sushi'
except TypeError as e:
    print(f"\n⚠️  Error: {e}")

# The restaurant changes its menu, replacing two items
foods = (
    'sushi',
    'burger',
    'pasta',
    'steak',
    'soup'
)

# Use a for loop to print each item on the revised menu
print("\n📋 Revised Menu:")
for food in foods:
    print(f"  • {food.title()}")

print("\n" + "=" * 50 + "\n")
