# Given the following data structure, write some code to return a list that
# contains the colors of the fruits and the sizes of the vegetables.
# The sizes should be uppercase, and the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# result = []

# for item in dict1.values():
#     if item['type'] == 'fruit':
#         result.append([colour.capitalize() for colour in item['colors']])
#     else:
#         result.append(item['size'].upper())

# Comprehension and Ternary expression:

def capitalize_string_elements(lst):
    return [item.capitalize() for item in lst]

result = [capitalize_string_elements(item['colors']) if item['type'] == 'fruit'
          else item['size'].upper() 
          for item in dict1.values()]

# Readable version?

def capitalize_string_elements(lst):
    return [item.capitalize() for item in lst]

def transform_item(item): # Outsourcing the if/else to a function!
    if item['type'] == 'fruit':
        return capitalize_string_elements(item['colors'])
    else:
        return item['size'].upper()

result = [transform_item(item) for item in dict1.values()]

print(result == [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"])
# PCODE:
# - Create an empty lst
# - Iterate through the original dict
# - for each item:
    # - if 'type' = 'fruit': get the colors
        # - iterate through the colours list and capitalize each word
        # - add this list with the transformed colours to the empty lst
    # - if 'type' = 'vegetable': get the 'size'
        # - change the value of 'size' into an all uppercase string
        # - add this string to the empty string



# Expected output:
[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]