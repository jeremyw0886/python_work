# learning_python.py
from pathlib import Path

# Method 1: Read the entire file at once
path = Path('text_files/learning_python.txt')
contents = path.read_text()
print("Reading the entire file at once:")
print(contents)

# Method 2: Read the file line by line
print("\nLooping over lines:")
lines = path.read_text().splitlines()
for line in lines:
    print(line)