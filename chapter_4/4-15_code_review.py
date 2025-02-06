# Using PEP 8 - revised 4-11_my_pizza_your_pizza.py
print("\n" + "=" * 50)
print("PIZZA COMPARISON".center(50))
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
print("PIZZA VARIETIES".center(50))
print("=" * 50 + "\n")

# List of different types of pizzas
pizzas = [
    'supreme',
    'caesar',
    'cheese',
    'pepperoni',
    'margherita',
    'bbq chicken',
    'hawaiian'
]

# Loop through the list and print a message for each pizza
for pizza in pizzas:
    print(f"💫 I like {pizza.title()} pizza.")

# Print the first three items in the list
print("\n📍 The first three items in the list are:")
print(f"  {', '.join(pizzas[:3]).title()}")

# Print three items from the middle of the list
print("\n📍 Three items from the middle of the list are:")
print(f"  {', '.join(pizzas[2:5]).title()}")

# Print the last three items in the list
print("\n📍 The last three items in the list are:")
print(f"  {', '.join(pizzas[-3:]).title()}")

# Print a final message
print("\n💝 I really love pizza!")

print("\n" + "=" * 50)
print("PETS".center(50))
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
print("\n💖 Any of these animals would make a great pet!")
print("\n" + "=" * 50 + "\n")
