# cats_and_dogs.py
from pathlib import Path

# List of files to read
files = ['text_files/cats.txt', 'text_files/dogs.txt']

for file in files:
    path = Path(file)
    try:
        contents = path.read_text()
        print(f"\nContents of {file}:")
        print(contents.rstrip())
    except FileNotFoundError:
        print(f"Sorry, the file '{file}' was not found.")