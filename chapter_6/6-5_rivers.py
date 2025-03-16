# Dictionary containing rivers and countries
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

# Loop through the dictionary and print the river and country
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Loop through the dictionary and print the river names
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Loop through the dictionary and print the country names
print("\nCountries:")
for country in rivers.values():
    print(country.title())
