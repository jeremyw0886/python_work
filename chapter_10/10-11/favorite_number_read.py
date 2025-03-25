# favorite_number_read.py
from pathlib import Path
import json

def get_stored_number(path):
    """Get stored favorite number if available."""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None

def display_number():
    """Display the user's favorite number."""
    path = Path('favorite_number.json')
    number = get_stored_number(path)
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        print("Sorry, I couldn't find your favorite number file.")

display_number()