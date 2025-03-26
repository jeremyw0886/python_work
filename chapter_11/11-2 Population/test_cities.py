# 11-1 City, Country/test_cities.py
from city_functions import city_country


def test_city_country():
    """Test that city_country() returns 'City, Country' format."""
    formatted_location = city_country("santiago", "chile")
    assert formatted_location == "Santiago, Chile"


def test_city_country_population():
    """Test that city_country() includes population when provided."""
    formatted_location = city_country("santiago", "chile", population=5000000)
    assert formatted_location == "Santiago, Chile - population 5000000"
