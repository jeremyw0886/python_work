def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current = messages.pop(0)
        print(current)
        sent_messages.append(current)


# List of short text messages and empty sent_messages list
texts = ["hey, how's it going?", "call me later", "meet at 5pm", "lol nice"]
sent_messages = []

# Call the function with a copy of the texts list
send_messages(texts[:], sent_messages)

# Print both lists to verify
print("\nOriginal list (texts):", texts)
print("Sent messages:", sent_messages)
