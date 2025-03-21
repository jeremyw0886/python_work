# admin_privileges.py
from user import User


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


class Admin(User):
    """A model for an admin user, inheriting from User."""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize parent attributes and privileges instance."""
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges()
