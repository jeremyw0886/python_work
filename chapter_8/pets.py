# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='willie', animal_type='dog')

def descirbe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


descirbe_pet(pet_name='willie')
descirbe_pet(pet_name='harry', animal_type='hamster')
