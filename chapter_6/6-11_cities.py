# Define a dictionary of cities with their details
cities = {
    'tokyo': {
        'country': 'japan',
        'population': '13,960,000',
        'fact': 'Home to the busiest pedestrian crossing in the world.'
    },

    'lagos': {
        'country': 'nigeria',
        'population': '15,000,000',
        'fact': 'Largest city in Africa by population.'
    },
    
    'new york': {
        'country': 'united states',
        'population': '8,300,000',
        'fact': 'Known as the city that never sleeps.'
    }
}

# Loop through the dictionary and print each city's information
for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"\tCountry - {info['country'].title()}")
    print(f"\tPopulation - {info['population']}")
    print(f"\tFact - {info['fact']}")
