# List of current users
current_users = ['alice', 'bob', 'charles', 'dave', 'eve', 'frank']

# List of new users
new_users = ['FRANK', 'Bob', 'Charlie', 'Hank', 'Ivy']

# Convert current users to lowercase
current_users_lower = [user.lower() for user in current_users]

# Loop through the new users and check for availability
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please choose a different one.")
    else:
        print(f"The username '{new_user}' is available.")
