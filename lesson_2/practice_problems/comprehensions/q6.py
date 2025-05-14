# Given the following data structure, return a new list identical in structure
# to the original but, with each number incremented by 1. Do not modify the
# original data structure. Use a comprehension.

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# new_lst = list(lst)
# for nested_dict in new_lst:
#     for key in nested_dict:
#         nested_dict[key] += 1

# Comprehension:

# def increment_values(dictionary):
#     return {item : dictionary[item] + 1 for item in dictionary}

# new_lst = [increment_values(subdict) for subdict in lst]

# Single comprehension:

new_lst = [{item : dictionary[item] + 1 for item in dictionary} # Expression (another comprehension) of value passed from outer comprehension
           for dictionary in lst]

# You create a dictionary using an inner comprehension first, which is the expression
# of the value passed from the lst in the outer comprehension

print(new_lst == [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}])
        

# Expected result:
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]