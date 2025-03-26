def get_formatted_name(frist, last, middle=""):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{frist} {middle} {last}"
    else:
        full_name = f"{frist} {last}"
    return full_name.title()
