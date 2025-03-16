guests = ["William Shakesbeer", "Plato Chips", "Isaac Neutron", "Stephen Hawk-King"]
print(f"Welcome to my literary and scientific pun-filled dinner party!")
print(f"This is the original guest list: \n\t{', '.join(guests)}.\n")

guests = sorted(guests)
print(f"To ensure order, I've decided to seat them alphabetically by first name:")
print(f"\tSeating Plan: \n\t\t{', '.join(guests)}.\n")

guests.append("Edgar Allan Yo")
print(f"I couldn't resist inviting {guests[-1]} as well, he has been 'raven' about it.\n")

guests.append("Mark Twang")
print(f"Oh, and {guests[-1]} is strumming his way to the list too.\n")

guests = sorted(guests)
print(f"With our new additions, here's the final guest list:")
print(f"\tFinalized Guest List: \n\t\t{', '.join(guests)}.\n")

guests = sorted(guests, reverse=True)
print(f"I've decided to seat them in reverse alphabetical order by first name:")
print(f"\tRevised Seating Plan: \n\t\t{', '.join(guests)}.\n")
