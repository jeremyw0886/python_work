def make_shirt(size, message):
    """Summarize a shirt's size and printed message."""
    print(f"The shirt is size {size} and has the message '{message}' "
          "printed on it.")


# Call with positional arguments
make_shirt('M', 'Cool Design')

# Call with keyword arguments
make_shirt(size='S', message='I love C++')
