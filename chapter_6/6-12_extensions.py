print("🌍 Welcome to Your Travel Planning Assistant! 🧳\n")
print("Here are some exciting destinations to consider:\n")

cities = {
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'Home to the busiest pedestrian crossing in the world.',
        'continent': 'asia',
        'famous_landmark': 'Tokyo Tower'
    },
    'lagos': {
        'country': 'nigeria',
        'population': '15 million',
        'fact': 'Largest city in Africa by population.',
        'continent': 'africa',
        'famous_landmark': 'National Theatre'
    },
    'new york': {
        'country': 'united states',
        'population': '8.3 million',
        'fact': 'Known as the city that never sleeps.',
        'continent': 'north america',
        'famous_landmark': 'Statue of Liberty'
    }
}

for city, info in cities.items():
    print(f"✈️  Destination: {city.title()}")
    print(f"📍 Located in: {info['country'].title()}")
    print(f"👥 Population: {info['population']}")
    print(f"💡 Travel Tip: {info['fact']}")
    print(f"🏛️  Landmark: {info['famous_landmark']}")
    print(f"🌎 Continent: {info['continent'].title()}")
    print("\n" + "="*50 + "\n")

print("Which destination sparks your wanderlust? 🤔")
