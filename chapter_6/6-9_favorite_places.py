# Define a dictionary of favorite places for each person
favorite_places = {
    'maya': ['Tokyo', 'Paris'],
    'leo': ['New York', 'London', 'Sydney'],
    'zara': ['Cairo']
}

# Loop through the dictionary and print each person's favorite places
for name, places in favorite_places.items():
    if len(places) == 1:
        places_str = places[0]
        print(f"{name.title()}'s favorite place is {places_str}.")
    elif len(places) == 2:
        places_str = ' and '.join(places)
        print(f"{name.title()}'s favorite places are {places_str}.")
    else:
        places_str = ', '.join(places[:-1]) + ', and ' + places[-1]
        print(f"{name.title()}'s favorite places are {places_str}.")
