# List of usernames
usernames = ['admin', 'alice', 'bob', 'charlie', 'dave']

# Loop through the list an print a greeting
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in.")
