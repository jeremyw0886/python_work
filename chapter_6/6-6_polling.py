# names of the people who took the poll and their favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# list of poll takers
poll_takers = ['jen', 'phil', 'mike', 'lisa']

# Loop through the poll takers and check if they have taken the poll
for name in poll_takers:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thanks for responding")
    else:
        print(f"{name.title()}, please take our poll!")
