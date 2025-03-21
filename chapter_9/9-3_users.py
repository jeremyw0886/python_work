class User:
    """A model for a user profile."""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize user attributes with proper capitalization."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.occupation = occupation

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile for {self.first_name} {self.last_name}:")
        print(f"- Age: {self.age}")
        print(f"- Location: {self.location}")
        print(f"- Occupation: {self.occupation}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(
            f"Hello, {self.first_name}! Nice to see you from {self.location}!"
        )


# Create three user instances
user1 = User("jeremy", "warren", 38, "hendersonville", "software developer")
user2 = User("maya", "chen", 25, "seattle", "graphic designer")
user3 = User("leo", "martinez", 42, "miami", "chef")

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
