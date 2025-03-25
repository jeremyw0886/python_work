# guest.py
from pathlib import Path

# Prompt user for their name
name = input("Please enter your name: ")

# Write the name to guest.txt
path = Path('text_files/guest.txt')
path.write_text(name)