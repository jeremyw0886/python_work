# 11-1 City, Country/city_functions.py
def city_country(city, country, population=None):
    """Return a string in the format 'City, Country, population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"
