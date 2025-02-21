# Define dictionaries for each pet
pet_1 = {
    'animal_type': 'dog',
    'owner': 'Alice',
}

pet_2 = {
    'animal_type': 'cat',
    'owner': 'Bob',
}

pet_3 = {
    'animal_type': 'parrot',
    'owner': 'Clara',
}

# Create a list of pets
pets = [pet_1, pet_2, pet_3]

# Loop through the list of pets and print their information
for pet in pets:
    print(f"Info about {pet['owner']}'s pet:")
    for key, value in pet.items():
        # Format and print key-value pairs
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print()
