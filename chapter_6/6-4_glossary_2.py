# Creates a dictionary of programming terms and their definitions
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
            'often using for or while to iterate over items or conditions.',
    'Dictionary': 'An unordered, mutable collection of key-value pairs '
                  'enclosed in curly braces, allowing fast lookups and changes.',
    'Tuple': 'An ordered, immutable collection of items (elements) enclosed '
             'in parentheses, allowing duplicates but not changes.',
    'Set': 'An unordered, mutable collection of unique items enclosed in '
           'curly braces, allowing fast membership tests and operations.',
    'Function': 'A named block of code that performs a specific task or '
                'returns a value, often with parameters and return values.',
    'Module': 'A file containing Python code, which can define functions, '
                'classes, and variables, and be imported into other programs.'      
}

# Loop through the dictionary and print the term and definition
for term, definition in glossary.items():
    print(f"{term}: {definition}\n")
