# Create a list of sandwich orders and an empty list for finished sandwiches
# Loop through orders, print a message, and move each to finished_sandwiches
# Finally, list all sandwiches that were made

sandwich_orders = ["tuna", "ham and cheese", "turkey", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # Take the first order
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a summary of all finished sandwiches
print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
