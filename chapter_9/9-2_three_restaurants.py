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


# Create three restaurant instances
restaurant1 = Restaurant("Bella Italia", "Italian")
restaurant2 = Restaurant("Sushi Haven", "Japanese")
restaurant3 = Restaurant("Taco Loco", "Mexican")

# Call describe_restaurant() for each
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
