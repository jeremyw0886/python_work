# Print the header for the dinner party
print("\n" + "✧･ﾟ" + "="*75 + "･ﾟ✧")
print("★ The Great Minds Dinner Party ★".center(79))
print("Adventures in Intellectual Entertainment".center(79))
print("Chapter 1: The Assembly of Brilliance".center(79))
print("✧･ﾟ" + "="*75 + "･ﾟ✧\n")

# Initial guest list
guests = ["William Shakesbeer", "Plato Chips", "Isaac Neutron", 
          "Stephen Hawk-King"]

# Print the initial gathering scene
print("🎭 Scene I: The Initial Gathering")
print("Our tale begins with an ambitious plan to unite the greatest"
      " (pun-ified) minds")
print("in history for an evening of wit, wisdom, and wonderfully terrible "
      "wordplay.\n")

# Print the original cast of characters
print("📜  The Original Cast of Characters:")
for guest in guests:
    print(f"\t✨ {guest}")

# First arrangement - alphabetical order and initial invitations
print("\n📋  Act I: The Order of Things")
print("For harmony's sake, our characters take their positions alphabetically:")
guests = sorted(guests)
print(f"\t🪑 {' ➜ '.join(guests)}")

# Print initial invitations
print("\n✉️   Initial Invitations:")
for guest in guests:
    print(f"\n  Dear {guest},")
    print("\tYou are cordially invited to an evening of intellectual "
          "brilliance!\n")

# First addition - Edgar Allan Yo
print("🌟  Plot Twist I: A Poetic Arrival")
guests.append("Edgar Allan Yo")
print(f"What's this? {guests[-1]} appears at our door!")
print("'Quoth the raven, let me party some more!'\n")

# Second addition - Mark Twang
print("🎸  Plot Twist II: A Musical Interlude")
guests.append("Mark Twang")
print(f"But wait! Here comes {guests[-1]}, strumming his way into our story,")
print("adding some rhythm to our intellectual revelry!\n")

# Updated guest list after initial additions
print("📚  Chapter Update: The Expanded Ensemble")
print("Our cast of characters has grown more illustrious:")
guests = sorted(guests)
for guest in guests:
    print(f"\t🌟 {guest}")

# Someone can't make it
print("😔  Unfortunate News")
print("Alas! Isaac Neutron can't make it - a case of quantum queasiness!\n")

# Replace guest and send revised invitations
guests.remove("Isaac Neutron")
guests.append("Charles Darwing")

print("✉️   Revised Invitations:")
for guest in guests:
    print(f"\n  Dear {guest},")
    print("\tYou are invited to our slightly altered evening of wit and "
          "wisdom!\n")

# Bigger table announcement
print("✧･ﾟ" + "="*75 + "･ﾟ✧")
print("🎊 BREAKING NEWS! 🎊".center(79))
print("Our dinner table has magically expanded!".center(79))
print("We can invite more brilliant minds!".center(79))
print("✧･ﾟ" + "="*75 + "･ﾟ✧\n")

# Add new guests
new_guests = ["Albert Finestein", "Marie Curry", "Leonardo da Veggie"]
print("✨ Introducing Our New Luminaries ✨")
for guest in new_guests:
    print(f"\n\t🌟 {guest}")
    match guest:
        case "Albert Finestein":
            print("\t'A relativity delicious evening is in your future!'")
        case "Marie Curry":
            print("\t'This party will be radiantly delicious!'")
        case "Leonardo da Veggie":
            print("\t'A renaissance of flavors awaits you!'")

# Add new guests to list
guests.insert(0, new_guests[0])      # Add to beginning
guests.insert(len(guests)//2, new_guests[1])  # Add to middle
guests.append(new_guests[2])         # Add to end

# Print final invitations for all guests
print("✉️   Final Invitations for All Guests:")
for guest in guests:
    print(f"\n  Dear {guest},")
    print("\tYou are cordially invited to our expanded gathering of great "
          "minds!")
    print("\tAn evening of wit, wisdom, and wonderfully terrible puns "
          "awaits!\n")

# Final guest list analysis
print("🔍 Final Guest List Analysis")
print("\n  First Three Guests:")
print(f"\t⭐ {', '.join(guests[:3])}")
print("\n  Middle Three Guests:")
middle = len(guests)//2
print(f"\t⭐ {', '.join(guests[middle-1:middle+2])}")
print("\n  Last Three Guests:")
print(f"\t⭐ {', '.join(guests[-3:])}\n")

# Print the footer for the dinner party
print("✧･ﾟ" + "="*75 + "･ﾟ✧")
print("End of guest list planning - Let the party begin!".center(79))
print("✧･ﾟ" + "="*75 + "･ﾟ✧\n")
