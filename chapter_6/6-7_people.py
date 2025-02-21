person_0 = {
    'first_name': 'Bruce',
    'last_name': 'Wayne',
    'age': 35,
    'city': 'Gotham'
}

person_1 = {
    'first_name': 'Diana',
    'last_name': 'Prince',
    'age': 30,
    'city': 'Themyscira'
}

person_2 = {
    'first_name': 'Clark',
    'last_name': 'Kent',
    'age': 33,
    'city': 'Metropolis'
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"Info about {person['first_name']} {person['last_name']}:")
    for key, value in person.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print()
