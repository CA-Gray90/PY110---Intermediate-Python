# Write some code to create a list of every vowel (a, e, i, o, u) that appears
# in the contained strings, then print it.

# Try to use a single comprehension

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

def list_of_vowels(dictionary):
    VOWELS = 'aeiou'

    return [char for lst in dictionary.values()
                for word in lst
                for char in word if char in VOWELS]

    # result = []

    # for lst in dictionary.values():
    #     for word in lst:
    #         for char in word:
    #             if char in VOWELS:
    #                 result.append(char)
    
    # return result

print(list_of_vowels(dict1) == ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o'])