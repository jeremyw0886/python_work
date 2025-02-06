# List of players
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Print the first three players (index 0 to 2)
print(players[0:3])

# Print the first four players (index 0 to 3)
print(players[:4])

# Print players from the third player to the end (index 2 to end)
print(players[2:])

# Print the last three players
print(players[-3:])

# Print a message and the first three players on the team
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
