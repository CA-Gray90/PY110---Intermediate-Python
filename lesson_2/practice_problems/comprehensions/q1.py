# Compute and display the total age of the family's *male* members.
# Try working out the answer two ways: first with an ordinary loop,
# then with a comprehension.

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Loop:
total_age = 0

for details in munsters.values():
    if details['gender'] == 'male':
        total_age += details['age']

print(total_age)

# Comprehension:
total_age = sum([details['age'] for details in munsters.values()
                 if details['gender'] == 'male'])

print(total_age)
# Expected output: 444