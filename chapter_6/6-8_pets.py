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

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Info about {pet['owner']}'s pet:")
    for key, value in pet.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print()
