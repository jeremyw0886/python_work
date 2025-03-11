# printing_models.py
from printing_functions import print_models, show_completed_models

# List of designs and empty completed list
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call the imported functions
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
