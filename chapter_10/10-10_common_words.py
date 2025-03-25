# common_words.py
from pathlib import Path

# List of files to analyze
files = ['text_files/pride_and_prejudice.txt', 'text_files/tale_of_two_cities.txt']

for file in files:
    path = Path(file)
    try:
        # Read the entire file
        contents = path.read_text(encoding='utf-8')
        
        # Count 'the' (case-insensitive)
        the_count = contents.lower().count('the')
        
        # Count 'the ' (with space, case-insensitive)
        the_space_count = contents.lower().count('the ')
        
        # Print results
        print(f"\nAnalysis for {file}:")
        print(f"Occurrences of 'the': {the_count}")
        print(f"Occurrences of 'the ': {the_space_count}")
        print(f"Difference: {the_count - the_space_count}")
        
    except FileNotFoundError:
        print(f"Sorry, the file '{file}' was not found.")