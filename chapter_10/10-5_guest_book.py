# guest_book.py
from pathlib import Path

# Path to the guest book file inside text_files folder
path = Path("text_files/guest_book.txt")

# Ensure the text_files directory exists
path.parent.mkdir(exist_ok=True)

# Prompt for names and record visits
while True:
    name = input("Please enter your name (or 'quit' to stop): ")
    if name.lower() == "quit":
        break
    print(f"Welcome, {name}! Thanks for visiting!")
    # Append the name to the file with a newline
    contents = path.read_text() if path.exists() else ""
    updated_contents = contents + name + "\n"
    path.write_text(updated_contents)
