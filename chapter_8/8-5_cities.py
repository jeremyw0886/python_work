def describe_city(city, country='usa'):
    """Display a city and its country."""
    print(f"{city.title()} is in {country.title()}.")


# Call the function for three cities
describe_city('atlanta')
describe_city('asheville')
describe_city('london', 'england')
