# favorite_number.py
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

def get_new_number(path):
    """Prompt for and store a new favorite number."""
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    return number

def manage_number():
    """Manage the user's favorite number."""
    path = Path('favorite_number.json')
    number = get_stored_number(path)
    if number:
        print(f"I know your favorite number! It's {number}.")
    else:
        number = get_new_number(path)
        print(f"We'll remember your favorite number: {number}!")

manage_number()