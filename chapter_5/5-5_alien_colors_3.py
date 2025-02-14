# Game configuration
WIDTH = 79
BORDER = "=" * 79
DIVIDER = "-" * 79
STARS = "*" * 79

# Title display
print(f"\n{BORDER}")
print("👾 ALIEN SHOOTER: THE COSMIC COLOR CAPER 👾".center(79))
print(f"{BORDER}\n")

# Story introduction
STORY = f"""
{'🌎 Earth News Network Breaking Report 🌎'.center(WIDTH)}
-------------------------------------------------------------------------------
In a colorful turn of events, Earth is under attack by the most 'hue-morous' 
invasion force we've ever seen! These aliens aren't just out of this world - 
they're out of the crayon box! 

Our brave defender has been taking them down with some 'spec-tacular' shooting 
skills. Let's see how they scored...
"""
print(STORY)
print(f"{STARS}\n")

# Alien configuration
alien_points = {
    'green': {
        'points': 5, 
        'emoji': '🟢',
        'pun': "They're green with envy... of our shooting skills!"
    },
    'yellow': {
        'points': 10, 
        'emoji': '🟡',
        'pun': "Talk about a 'yellow belly'... they ran for the stars!"
    },
    'red': {
        'points': 15, 
        'emoji': '🔴',
        'pun': "These ones were caught RED handed!"
    }
}

# Game execution
total_points = 0
alien_colors = ['green', 'yellow', 'red']

for color in alien_colors:
    alien = alien_points[color]
    emoji = alien['emoji']
    points = alien['points']
    total_points += points
    kapow_message = f"{emoji}  KAPOW! {emoji}\n"
    
    print(kapow_message.center(WIDTH))
    print(f"You blasted a {color} alien for {points} points!")
    print(f"✨ {alien['pun']}")
    print(f"{DIVIDER}\n")

# Score summary
print("🏆 FINAL MISSION REPORT 🏆".center(WIDTH))
print(BORDER)
print(f"Total Points: {total_points}")
print(f"Aliens Defeated: {len(alien_colors)}")
print(BORDER)

# Closing message
CLOSING = f"""
{'🌟 Mission Accomplished! 🌟'.center(WIDTH)}
------------------------------------------------------------------------------- 
Thanks for saving Earth, you're out of this world!
"""
print(CLOSING)
