# Ask for age and calculate ticket price
# Loop stops when user enters 'quit' in the while condition
# age_input = ""
# while age_input != "quit":
#     age_input = input("Enter your age (or 'quit' to finish): ")
#     if age_input == "quit":
#         age = int(age_input)
#         if age < 3:
#             print("Your ticket is free.")
#         elif age < 13:
#             print("Your ticket is $10.")
#         else:
#             print("Your ticket is $15.")

# Ask for age and calculate ticket price
# Use an active variable to control the loop
# active = True
# while active:
#     age_input = input("Enter your age (or 'quit' to finish): ")
#     if age_input == "quit":
#         active = False
#     else:
#         age = int(age_input)
#         if age < 3:
#             print("Your ticket is free.")
#         elif age < 13:
#             print("Your ticket is $10.")
#         else:
#             print("Your ticket is $15.")

# Ask for age and calculate ticket price
# Use break to exit when user enters 'quit'
while True:
    age_input = input("Enter your age (or 'quit' to finish): ")
    if age_input == "quit":
        break
    else:
        age = int(age_input)
        if age < 3:
            print("Your ticket is free.")
        elif age < 13:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
