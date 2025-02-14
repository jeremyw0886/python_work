# Assigns age of a person
age = 25

# Determines the stage of life based on age
if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

# Prints the stage of life
print(f"You are a {stage}.")
