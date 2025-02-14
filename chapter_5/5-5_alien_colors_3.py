# Define alien colors and corresponding points
alien_points = {
    'green': 5,
    'yellow': 10,
    'red': 15
}

# List of alien colors
alien_colors = ['green', 'yellow', 'red']

# Loop through the list and print the points
for color in alien_colors:
    print(f"You just earned {alien_points[color]} points for shooting a {color} alien!")
