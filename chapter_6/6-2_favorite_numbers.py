# This program stores favorite numbers in a dictionary.
favorite_numbers = {
    'Earl E. Bird' : 6,
    'Penny Tration' : 1,
    'Forrest Runner' : 26,
    'Carrie Oakey' : 88,
    'Will Power' : 100
    }

# Loop through the dictionary and print the name and favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
