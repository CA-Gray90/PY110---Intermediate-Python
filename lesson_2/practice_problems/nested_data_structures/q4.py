# Given the object shown below, print the name, age, and gender of each family member:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for name in munsters:
    age = munsters[name]['age']
    gender = munsters[name]['gender']

    print(f'{name} is a {age}-year-old {gender}.')



# LS Solution:
# for name, details in munsters.items(): # -> tuple unpacking
#     print(f'{name} is a {details['age']}-year-old {details['gender']}')

# Test Case results:
# Herman is a 32-year-old male.
# Lily is a 30-year-old female.
# Grandpa is a 402-year-old male.
# Eddie is a 10-year-old male.
# Marilyn is a 23-year-old female.