# List of different types of pizzas
pizzas = ['supreme', 'caesar', 'cheese', 'pepperoni', 'margherita', 'bbq chicken', 'hawaiian']

# Loop through the list and print a message for each pizza
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# Print the first three items in the list
print("The first three items in the list are:")
print(pizzas[:3])  # Slicing the list to get the first three items

# Print three items from the middle of the list
print("Three items from the middle of the list are:")
print(pizzas[2:5])  # Slicing the list to get three items from the middle

# Print the last three items in the list
print("The last three items in the list are:")
print(pizzas[-3:])  # Slicing the list to get the last three items

# Print a final message
print("I really love pizza!")
