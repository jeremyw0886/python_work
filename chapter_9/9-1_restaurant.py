class Restaurant:
    """A simple restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display restaurant name and cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.restaurant_name} is open for business!")


# Test the class
my_restaurant = Restaurant("Bella Italia", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
