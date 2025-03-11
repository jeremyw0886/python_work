def make_sandwich(*items):
    """Summarize a sandwich with a variable number of items."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


# Call the function three times with different numbers of arguments
make_sandwich('turkey', 'cheddar', 'lettuce')
make_sandwich('ham', 'swiss')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')
