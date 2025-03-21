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


class Admin(User):
    """A model for an admin user, inheriting from User."""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize parent attributes and privileges instance."""
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges()


class Privileges:
    """A class to store and manage admin privileges."""

    def __init__(self):
        """Initialize the privileges attribute."""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can view all users",
        ]

    def show_privileges(self):
        """Print the privileges of the admin."""
        print("\nAdmin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create an instance of Admin and test
admin = Admin("jeremy", "warren", 38, "hendersonville", "software developer")
admin.describe_user()
admin.privileges.show_privileges()
