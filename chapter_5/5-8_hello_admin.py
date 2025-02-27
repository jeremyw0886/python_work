# List of usernames
usernames = ['admin', 'alice', 'bob', 'charlie', 'dave']

# Loop through the list an print a greeting
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in.")

print('\n')

# List of temperatures
temps = [17, 32, 65]

# Convert the list into a dictionary with corresponding messages
temp_messages = {
    17: "too freakin' cold",
    32: "freezing but bearable",
    65: "a nice temperature"
}

# Print out the messages for each temperature
for temp in temps:
    print(f"{temp} degrees is {temp_messages[temp]}")
