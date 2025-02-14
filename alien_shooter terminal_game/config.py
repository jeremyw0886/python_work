# Game settings
GAME_WIDTH = 32  # Reduced width to account for emoji width
GAME_HEIGHT = 20

TITLE = """
╔═══════════════════════════╗
║    🚀 ALIEN SHOOTER 👾    ║
╚═══════════════════════════╝"""

CONTROLS = """
╔════════ HOW TO PLAY ════════╗
║                             ║
║  ← → Arrow Keys to Move     ║
║  SPACE to Shoot             ║
║  Q to Quit                  ║
║                             ║
║  ALIEN POINTS:              ║
║  🟢 Green  = 5  (Common)    ║
║  🟡 Yellow = 10 (Uncommon ) ║
║  🔴 Red    = 15 (Rare)      ║
║                             ║
║  Stop the aliens!           ║
╚═════════════════════════════╝"""

# Game characters
PLAYER_CHAR = "🚀"
BULLET_CHAR = "│"
EMPTY_CHAR = " "

# Game borders
TOP_BORDER    = "╔" + "═" * (GAME_WIDTH - 2) + "╗"
BOTTOM_BORDER = "╚" + "═" * (GAME_WIDTH - 2) + "╝"
SIDE_BORDER   = "║"

# Game settings
FRAME_RATE = 0.1
ALIEN_SPAWN_RATE = 0.05
ALIEN_MOVE_COUNTER = 5

# Alien types
ALIENS = {
    'green': {
        'char': '🟢',
        'points': 5,
        'weight': 50
    },
    'yellow': {
        'char': '🟡',
        'points': 10,
        'weight': 30
    },
    'red': {
        'char': '🔴',
        'points': 15,
        'weight': 20
    }
}
