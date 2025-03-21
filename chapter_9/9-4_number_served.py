class Restaurant:
    """A simple restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type, and number served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display restaurant name and cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Simulate opening the restaurant."""
        print(f"{self.restaurant_name} is open for business!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, increment):
        """Increment the number of customers served."""
        self.number_served += increment


# Create an instance
restaurant = Restaurant("Bella Italia", "Italian")

# Print initial number served
print(f"Number of customers served today: {restaurant.number_served}")

# Change and print again
restaurant.number_served = 50
print(f"Number of customers served today: {restaurant.number_served}")

# Set a new number with the method and print
restaurant.set_number_served(100)
print(f"Number of customers served today: {restaurant.number_served}")

# Increment with a day's worth of customers and print
restaurant.increment_number_served(25)
print(f"Number of customers served today: {restaurant.number_served}")
