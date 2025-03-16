# Create sandwich orders list with pastrami appearing multiple times
# Remove pastrami after announcing shortage, then process orders
# Track and list finished sandwiches

sandwich_orders = ["tuna", "pastrami", "ham and cheese", "pastrami",
                   "turkey", "pastrami", "veggie"]
finished = []

# Announce pastrami shortage and remove all pastrami orders
print("Sorry, the deli has run out of pastrami!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Process remaining sandwich orders
while sandwich_orders:
    current = sandwich_orders.pop(0)
    print(f"I made your {current} sandwich.")
    finished.append(current)

# Print summary of finished sandwiches
print("\nAll sandwiches made:")
for sandwich in finished:
    print(f"- {sandwich}")
