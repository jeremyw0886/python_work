import os
import time
from game import Game
from config import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_instructions():
    clear_screen()
    print(TITLE)
    print(CONTROLS)
    input("\nPress Enter to return to menu...")

def main():
    while True:
        clear_screen()
        print(TITLE)
        print("\n1. Start Game")
        print("2. Instructions")
        print("3. Quit")
        
        choice = input("\nSelect option (1-3): ")
        
        if choice == '1':
            game = Game()
            game.start()
        elif choice == '2':
            show_instructions()
        elif choice == '3':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
