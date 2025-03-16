# Ask the user how many people are in their dinner group
# and store it as an integer
group_size = int(input("How many people are in your dinner group? "))

if group_size > 8:
    print("\nI'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
