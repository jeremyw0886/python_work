# test_employee.py
import pytest
from employee import Employee


@pytest.fixture
def employee():
    """Return an employee with default attributes."""
    return Employee("everyone", "else")


@pytest.fixture
def best_employee():
    """Return best employee ever."""
    return Employee("jeremy", "warren")


def test_give_default_raise(employee):
    """Test the default raise increases salary by $5000."""
    employee.give_raise()
    assert employee.salary == 5000


def test_give_custom_raise(best_employee):
    """Test that a custom raise increases salary by that amount."""
    best_employee.give_raise(1000000)
    assert best_employee.salary == 1000000
