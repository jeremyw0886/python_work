import random
import time
import os
import sys
import msvcrt

from config import *

class Game:
    def __init__(self):
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        self.score = 0
        self.player_pos = (self.width - 2) // 2
        self.aliens = []
        self.bullets = []
        self.game_over = False
        self.move_counter = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_random_alien_type(self):
        weights = [ALIENS[type]['weight'] for type in ALIENS]
        types = list(ALIENS.keys())
        return random.choices(types, weights=weights)[0]

    def get_string_width(self, s):
        """Calculate visual width of string, counting emojis as single width"""
        width = 0
        for char in s:
            if char in '🚀👾🟢🟡🔴':  # List of all emoji characters used
                width += 1  # Count emoji as single width for padding
            else:
                width += 1
        return width

    def pad_line(self, line, target_width):
        """Pad line to target width, accounting for emoji width"""
        visual_width = self.get_string_width(line)
        padding_needed = target_width - visual_width
        if padding_needed < 0:
            padding_needed = 0
        return line + (EMPTY_CHAR * padding_needed)

    def get_key(self):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            try:
                # Handle arrow keys
                if key == b'\xe0':  # Special key prefix
                    key = msvcrt.getch()
                    if key == b'K':  # Left arrow
                        return 'left'
                    elif key == b'M':  # Right arrow
                        return 'right'
                else:
                    return key.decode('utf-8').lower()
            except:
                return None
        return None

    def draw_screen(self):
        # Create empty screen with fixed width
        display_width = self.width - 2  # Account for borders
        screen = [[EMPTY_CHAR for x in range(display_width)] 
                 for y in range(self.height)]
        
        # Draw player
        player_pos = min(self.player_pos, display_width - 1)
        screen[-1][player_pos] = PLAYER_CHAR
        
        # Draw aliens
        for alien in self.aliens:
            x, y, alien_type = alien
            if 0 <= y < self.height and 0 <= x < display_width:
                screen[y][x] = ALIENS[alien_type]['char']
        
        # Draw bullets
        for bullet in self.bullets:
            x, y = bullet
            if 0 <= y < self.height and 0 <= x < display_width:
                screen[y][x] = BULLET_CHAR
        
        # Print game state
        self.clear_screen()
        print(TITLE)
        
        # Print score
        score_text = f"Score: {self.score}"
        print(TOP_BORDER)
        print(f"{SIDE_BORDER}{score_text:<{display_width}}{SIDE_BORDER}")
        print(BOTTOM_BORDER)
        
        # Draw game area
        print(TOP_BORDER)
        for row in screen:
            line = ''.join(row)
            padded_line = self.pad_line(line, display_width)
            print(f"{SIDE_BORDER}{padded_line}{SIDE_BORDER}")
        print(BOTTOM_BORDER)

    def update(self):
        # Update bullets
        self.bullets = [(bx, by-1) for bx, by in self.bullets if by > 0]
        
        # Update aliens
        self.move_counter += 1
        if self.move_counter >= ALIEN_MOVE_COUNTER:
            self.move_counter = 0
            new_aliens = []
            for ax, ay, alien_type in self.aliens:
                if ay < self.height - 1:
                    new_aliens.append((ax, ay + 1, alien_type))
                else:
                    self.game_over = True
            self.aliens = new_aliens

        # Check collisions
        for bullet in self.bullets[:]:
            for alien in self.aliens[:]:
                ax, ay, alien_type = alien
                if bullet[0] == ax and bullet[1] == ay:
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if alien in self.aliens:
                        self.aliens.remove(alien)
                        self.score += ALIENS[alien_type]['points']

    def process_input(self):
        key = self.get_key()
        if key:
            if key == 'left' and self.player_pos > 0:
                self.player_pos -= 1
            elif key == 'right' and self.player_pos < self.width - 3:
                self.player_pos += 1
            elif key == ' ':  # Spacebar
                self.bullets.append((self.player_pos, self.height-2))
            elif key == 'q':
                self.game_over = True

    def start(self):
        while not self.game_over:
            if random.random() < ALIEN_SPAWN_RATE:
                alien_type = self.get_random_alien_type()
                self.aliens.append((
                    random.randint(0, self.width-3), 
                    0, 
                    alien_type
                ))

            self.process_input()
            self.update()
            self.draw_screen()
            time.sleep(FRAME_RATE)

        # Game over screen
        game_over_text = "GAME OVER"
        score_text = f"Final Score: {self.score}"
        print(f"""
╔{'═' * (self.width-2)}╗
║{game_over_text.center(self.width-2)}║
║{score_text.center(self.width-2)}║
╚{'═' * (self.width-2)}╝
""")
        input("\nPress Enter to continue...")
