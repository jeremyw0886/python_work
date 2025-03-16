def city_country(city, country):
    """Return a city and its country."""
    return f"{city.title()}, {country.title()}"


# Call the function with different cities and countries
location = city_country('atlanta', 'usa')
print(location)

location = city_country('asheville', 'usa')
print(location)

location = city_country('london', 'england')
print(location)
