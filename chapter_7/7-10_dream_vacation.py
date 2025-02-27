# Poll users about their dream vacation spot and store responses
# Allow users to quit, then print all collected responses
responses = {}

# Poll loop: collect name and vacation spot
active = True
while active:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where "
                  "would you go? ")
    responses[name] = place
    again = input("Would you like to let someone else respond? "
                  "(yes/no) ")
    if again == "no":
        active = False

# Print poll results
print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")
