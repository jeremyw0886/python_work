# List of my favorite pizzas
my_pizzas = ['supreme', 'caesar', 'cheese']

# Make a copy of the list to represent my friend's favorite pizzas
friend_pizzas = my_pizzas[:]

# Add a new pizza to my list
my_pizzas.append('pepperoni')

# Add a different new pizza to my friend's list
friend_pizzas.append('margherita')

# Print my favorite pizzas
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

# Print my friend's favorite pizzas
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
