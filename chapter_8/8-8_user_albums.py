def make_album(artist, title):
    """Return a dictionary of information about an album."""
    album = {'artist': artist, 'title': title}
    return album


# Loop to collect user input for albums
print("Enter 'quit' at any time to quit.")
while True:
    artist = input("Artist name:")
    if artist.lower() == 'quit':
        break
    title = input("Album title:")
    album_info = make_album(artist.title(), title.title())
    print(album_info)
