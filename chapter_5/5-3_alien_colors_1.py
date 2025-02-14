# Version that passes the if test
alien_color = 'green'

if alien_color == 'green':
    print(f"You just earned 5 points for shooting a {alien_color} alien!")

# Version that fails the if test
alien_color = 'yellow'

if alien_color != 'yellow':
    print(f"You just earned 5 points for shooting a {alien_color} alien!")
