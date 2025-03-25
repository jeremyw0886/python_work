# favorite_number_write.py
from pathlib import Path
import json

def get_new_number(path):
    """Prompt for and store a new favorite number."""
    number = input("What's your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    return number

def store_number():
    """Store the user's favorite number."""
    path = Path('favorite_number.json')
    number = get_new_number(path)
    print(f"We've stored your favorite number: {number}")

store_number()