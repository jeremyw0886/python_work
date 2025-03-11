def make_album(artist, title):
    """Return a dictionary of information about an album."""
    album = {'artist': artist, 'title': title}
    return album


# Create and print three albums
print(make_album('the beatles', 'abbey road'))
print(make_album('pink floyd', 'dark side of the moon'))
print(make_album('led zeppelin', 'led zeppelin iv'))
