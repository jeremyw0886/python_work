# 11-1 City, Country/test_cities.py
from city_functions import city_country


def test_city_country():
    """Test that city_country() returns 'City, Country' format."""
    formatted_location = city_country("santiago", "chile")
    assert formatted_location == "Santiago, Chile"
