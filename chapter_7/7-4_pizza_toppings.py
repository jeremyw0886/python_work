# Prompt the user to enter pizza toppings one at a time
# Keep looping until they enter 'quit'
# Confirm each topping with a message
topping = ''
while topping != 'quit':
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
