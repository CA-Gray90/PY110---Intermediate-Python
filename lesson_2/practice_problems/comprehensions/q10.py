# Write a function that takes no arguments and returns a string that contains a UUID.
import random

HEX_DIGITS = '0123456789abcdef'
UUID_SECTION_SIZES = (8, 4, 4, 4, 12)

# def generate_uuid():
#     return '-'.join([get_hex_digits(length) for length in UUID_SECTION_SIZES])

# def get_hex_digits(length):
#     return ''.join([random.choice(HEX_DIGITS) for _ in range(length)])

def generate_uuid():
    return '-'.join([''.join([random.choice(HEX_DIGITS) for _ in range(length)]) for length in UUID_SECTION_SIZES])

print(generate_uuid())
print(generate_uuid())
print(generate_uuid())

# PCODE:
# SET a variable to a string containing the all possible hexidecimal digits
# SET a variable to a list containing 8, 4, 4, 4, 12 (The sections of a UUID)
# SET an empty list
# While LOOPING through the list of UUID sectinos sizes:
    # SET an empty string:
    # Concatenate random hex characters to the string till its length matches the current number in the list of UUID section numbers
    # append this string of hex chars to the empty list
    # Repeat steps with each number in the list of numbers

# Join together list of hex strings using '-'
# Return this string
