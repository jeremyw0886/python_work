import person
import person as p

# from person import *
from person import build_person
from person import build_person as bp

# Using the imported functions and modules
profile1 = person.build_person('jimi', 'hendrix', age=27)
print("1. Import module:", profile1)

profile2 = build_person('ada', 'lovelace', age=36)
print("2. Import specific:", profile2)

profile3 = bp('nikola', 'tesla', age=86)
print("3. Function alias:", profile3)

profile4 = p.build_person('marie', 'curie', age=66)
print("4. Module alias:", profile4)

profile5 = build_person('alan', 'turing', age=41)
print("5. Import all:", profile5)
