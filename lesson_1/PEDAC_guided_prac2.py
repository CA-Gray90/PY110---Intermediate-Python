# Sort strings by most adjacent consonants
def sort_by_consonant_count(lst):
    lst.sort(reverse=True, key=count_max_adjacent_consonants)
    return lst

def count_max_adjacent_consonants(string):
    VOWELS = 'aeiou'
    string = ''.join(char for char in string.casefold() if char.isalpha()) 
    adjacent_consonants = ''
    max_count = 0

    for char in string:
        if char not in VOWELS:
            adjacent_consonants += char
            if max_count < len(adjacent_consonants) > 1:
                max_count = len(adjacent_consonants)
        else:
            adjacent_consonants = ''

    return max_count

# LS Solution notes:
# using ''.join(string.split(' ')) to remove spaces, add .lower() method to lower case all chars

# Test Cases:

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan'] # 2, 0, 2, 3
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year'] # 0, 0, 3, 0
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb'] # 3, 4, 4
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])