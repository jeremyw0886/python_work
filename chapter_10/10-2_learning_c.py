# learning_c.py
from pathlib import Path

# Read the file and replace 'Python' with 'C'
path = Path('text_files/learning_python.txt')
lines = path.read_text().splitlines()

print("Lines with 'Python' replaced by 'C':")
for line in lines:
    modified_line = line.replace("Python", "C")
    print(modified_line)