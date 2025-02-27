# Display the header
print("\n==========================================")
print("         Welcome to Punchline Deli        ")
print("==========================================")

# Display the menu
print("\n          TODAY'S SPECIALS")
print("------------------------------------------")
print("  1. 🥖 Bread-y or Not")
print("  2. 🍖 Ham-azing Grace")
print("  3. 🦃 Turkey'n Twister")
print("  4. 🧀 Cheese Louise")
print("  5. 🥚 Egg-streme Yolkster")
print("------------------------------------------")

# Initialize orders and finished lists
orders = ["bread-y or not", "ham-azing grace", "turkey-ng twister",
          "cheese louise", "egg-streme yolkster"]
finished = []

# Display orders in progress
print("\n          ORDERS IN PROGRESS")
print("------------------------------------------")

# Process each order with custom messages
while orders:
    current = orders.pop(0)
    if "bread-y" in current:
        print(f"\n🥖 Kneading it fast, {current.upper()}!")
    elif "ham-azing" in current:
        print(f"\n🍖 Blessing it with flavor, {current.upper()}!")
    elif "turkey" in current:
        print(f"\n🦃 Spinning your {current.upper()}!")
    elif "cheese" in current:
        print(f"\n🧀 Look at all that {current.upper()}!")
    elif "egg-streme" in current:
        print(f"\n🥚 Cracking up for your {current.upper()}!")
    finished.append(current)

# Display completed orders with themed icons and messages
print("\n          COMPLETED ORDERS")
print("------------------------------------------")
for sandwich in finished:
    if "bread-y" in sandwich:
        print(f"\n🥖 {sandwich.title()}")
        print("   -Fresh from the oven!")
    elif "ham-azing" in sandwich:
        print(f"\n🍖 {sandwich.title()}")
        print("   -A divine delivery!")
    elif "turkey" in sandwich:
        print(f"\n🦃 {sandwich.title()}")
        print("   -Twisted to perfection!")
    elif "cheese" in sandwich:
        print(f"\n🧀 {sandwich.title()}")
        print("   -A gooey masterpiece!")
    elif "egg-streme" in sandwich:
        print(f"\n🥚 {sandwich.title()}")
        print("   -Sunny side up and ready!")

# Display the footer
print("\n------------------------------------------")
print("          Thank you for visiting!")
print("------------------------------------------")
