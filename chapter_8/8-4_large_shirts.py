def make_shirt(shirt_size='L', shirt_message='I love Python'):
    """Summarize a shirt's size and printed message."""
    print(f"The shirt is size {shirt_size} and has the message "
          f"'{shirt_message}' printed on it.")


# Call with positional arguments
make_shirt()                     # Large shirt, default message
make_shirt('M')                  # Medium shirt, default message
make_shirt('3t', 'I love Dad')   # Any size, custom message
