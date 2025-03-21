# 9-5_login_attempts.py
class User:
    """A model for a user profile."""

    def __init__(
        self,
        first_name,
        last_name,
        age,
        location,
        occupation,
        login_attempts=0,
    ):
        """Initialize user attributes with proper capitalization."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.occupation = occupation
        self.login_attempts = login_attempts

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

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to zero."""
        self.login_attempts = 0


# Create an instance
user = User("jeremy", "warren", 30, "asheville", "software developer")

# Print initial login attempts
print(f"Initial login attempts: {user.login_attempts}")

# Increment login attempts several times
user.increment_login_attempts()
print(f"After 1 attempt: {user.login_attempts}")
user.increment_login_attempts()
print(f"After 2 attempts: {user.login_attempts}")
user.increment_login_attempts()
print(f"After 3 attempts: {user.login_attempts}")

# Reset and print again
user.reset_login_attempts()
print(f"After reset: {user.login_attempts}")
