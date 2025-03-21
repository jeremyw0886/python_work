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


class IceCreamStand(Restaurant):
    """A simple model of an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize parent attributes and an empty flavors list."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self, flavors):
        """Add flavors to the ice cream stand."""
        self.flavors.extend(flavors)

    def display_flavors(self):
        """Display available ice cream flavors."""
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Test the instance
ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream")
ice_cream_stand.add_flavors(["Vanilla", "Chocolate", "Strawberry"])
ice_cream_stand.display_flavors()
