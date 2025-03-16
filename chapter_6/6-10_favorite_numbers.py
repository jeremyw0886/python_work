# This program stores favorite numbers in a dictionary.
favorite_numbers = {
    'Earl E. Bird': [6, 5],
    'Penny Tration': [1, 100],
    'Forrest Runner': [26, 13, 3],
    'Carrie Oakey': [88, 7],
    'Will Power': [100]
}

# Loop through the dictionary and print the name and favorite numbers
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        numbers_str = str(numbers[0])
        print(f"{name.title()}'s favorite number is {numbers_str}.")
    elif len(numbers) == 2:
        numbers_str = ' and '.join(str(number) for number in numbers)
        print(f"{name.title()}'s favorite numbers are {numbers_str}.")
    else:
        numbers_str = (
            ', '.join(str(number) for number in numbers[:-1]) + 
            ', and ' + str(numbers[-1]))
        print(f"{name.title()}'s favorite numbers are {numbers_str}.")
