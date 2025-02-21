# Creates a dictionary of programming terms and their definitions, then prints each term and definition.
glossary = {
    'Variable': 'A named storage location in memory that holds a value, '
                'which can be changed during program execution.',
    'String': 'A sequence of characters (letters, numbers, or symbols) '
              'enclosed in single or double quotes, used to represent text.',
    'List': 'An ordered, mutable collection of items (elements) enclosed '
            'in square brackets, allowing duplicates and changes.',
    'Index': 'A number representing the position of an item in a sequence '
             '(like a list or string), starting at 0 for the first item.',
    'Loop': 'A control structure that repeats a block of code multiple times,' 
            'often using for or while to iterate over items or conditions.'
}

for term, definition in glossary.items():
    print(f"{term}: {definition}\n")
