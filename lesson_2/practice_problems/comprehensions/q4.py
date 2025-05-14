# Given the following data structure, write some code that uses comprehensions
# to define a dictionary where the key is the first item in each sublist,
# and the value is the second.

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

new_dict = {sublist[0] : sublist[1] for sublist in lst}

print(new_dict == {
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
})

# Expected output:
# Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {'c': 3},
#     'D': ['a', 'b', 'c']
# }