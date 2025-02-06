# Create a list of multiples of three from 3 to 30
multiples_of_three = [number for number in range(3, 31) if number % 3 == 0]

# Loop through the list and print each multiple of three
for number in multiples_of_three:
    print(number)
