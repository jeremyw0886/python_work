# employee.py
class Employee:
    """A class representing an employee."""

    def __init__(self, first_name, last_name):
        """Initialize employee with frist name, last name, salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 0

    def give_raise(self, amount=5000):
        """Increase the emplyee's salary by a specified amount)"""
        self.salary += amount
