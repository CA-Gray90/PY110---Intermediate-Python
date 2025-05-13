# Given the following string, create a dictionary that represents the frequency
# with which each letter occurs. The frequency count should be case-sensitive:

statement = "The Flintstones Rock"

letter_count = {}

for char in statement:
    if char.isalpha(): # Selection
        letter_count[char] = letter_count.get(char, 0) + 1

print(letter_count)

# Alternate solution using .setdefault()

letter_count = {}

for char in statement:
    if char not in letter_count and char.isalpha():
        letter_count.setdefault(char, statement.count(char))

print(letter_count)

# Another solution:

letter_count = {}

for char in statement:
    if char.isalpha():
        letter_count.setdefault(char, 0)
        letter_count[char] += 1

print(letter_count)

# Pretty printed for clarity
# {
#     'T': 1,
#     'h': 1,
#     'e': 2,
#     'F': 1,
#     'l': 1,
#     'i': 1,
#     'n': 2,
#     't': 2,
#     's': 2,
#     'o': 2,
#     'R': 1,
#     'c': 1,
#     'k': 1
# }