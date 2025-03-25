# guest_book.py
from pathlib import Path

# Collect names in a list
names = []
while True:
    name = input("Please enter your name (or 'quit' to stop): ")
    if name.lower() == 'quit':
        break
    names.append(name)

# Write names to guest_book.txt, each on a new line
path = Path('text_files/guest_book.txt')
contents = '\n'.join(names)
path.write_text(contents)