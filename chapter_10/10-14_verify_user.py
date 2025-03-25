# verify_user_dict.py
from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for and store new user info."""
    user_info = {}
    user_info['username'] = input("What is your name? ")
    user_info['age'] = input("How old are you? ")
    user_info['favorite_color'] = input("What's your favorite color? ")
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    """Greet the user and manage their info, verifying the username."""
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    if user_info:
        response = input(f"Is {user_info['username']} your username? (yes/no): ")
        if response.lower() == 'yes':
            print(f"\nWelcome back, {user_info['username']}!")
            print("Here's what I remember about you:")
            print(f"- Username: {user_info['username']}")
            print(f"- Age: {user_info['age']}")
            print(f"- Favorite Color: {user_info['favorite_color']}")
        else:
            user_info = get_new_user_info(path)
            print(f"\nWe'll remember you when you come back, {user_info['username']}!")
            print("Here's what I've stored about you:")
            print(f"- Username: {user_info['username']}")
            print(f"- Age: {user_info['age']}")
            print(f"- Favorite Color: {user_info['favorite_color']}")
    else:
        user_info = get_new_user_info(path)
        print(f"\nWe'll remember you when you come back, {user_info['username']}!")
        print("Here's what I've stored about you:")
        print(f"- Username: {user_info['username']}")
        print(f"- Age: {user_info['age']}")
        print(f"- Favorite Color: {user_info['favorite_color']}")

greet_user()