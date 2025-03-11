def make_car(manufacturer, model, **car_info):
    """Build a dictionary with car details."""
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(car_info)
    return car


# Call the function with required and optional info
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the resulting dictionary
print(car)
