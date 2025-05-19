# Given the following data structure, write some code to return a list that
# contains only the dictionaries where all the numbers are even.

# - LS breakdown: We want to selectively include elements from the original
# data structure based on certain criteria.

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def get_dicts_with_even_values(lst):
    return [dictionary for dictionary in lst if all_even_dict(dictionary)]

def all_even_list(lst):
    return all([num % 2 == 0 for num in lst])

def all_even_dict(dictionary):
    return all([all_even_list(nums_list) for nums_list in dictionary.values()])

print(get_dicts_with_even_values(lst))

# print(check_if_all_even([1, 2, 3]) == False)
# print(check_if_all_even([1, 2, 4]) == False)
# print(check_if_all_even([6, 2, 4]) == True)

# PCODE:
# Initialize emtpy list
# For dict in lst:
    # for values (lists) in each dict:
        # Iterate through the numbers in each list value and check whether all of
        # the numbers are even:
            # 1. Initialize empty list, for each number, if it is even, append
            # True to the empty list, else False
            # Use `all()` to check whether all values are even (True)
        # IF they are ALL even in the dict, append that dict to the result list

## Original solution:

# for dictionary in lst:
#     print(dictionary)
#     result = []
#     for numbers_list in dictionary.values():
#         result.append(check_if_all_even(numbers_list))
#         print(result)
#     if all(result):
#         even_dicts.append(dictionary)
#         print(even_dicts)

## Second refactored solution:
# def get_dicts_with_even_values(lst):
#     return [inner_dict for inner_dict in lst
#               if all([check_if_all_even(numbers_list)
#                       for numbers_list in inner_dict.values()])]

# def check_if_all_even(lst):
#     return all([num % 2 == 0 for num in lst])

# print(get_dicts_with_even_values(lst))

## LS Solution:
# def list_is_even(lst):
#     return all([num % 2 == 0 for num in lst])

# def all_even(dictionary):
#     lists_are_even = [list_is_even(list_value)
#                       for list_value in dictionary.values()]
#     return all(lists_are_even)

# result = [dictionary for dictionary in lst
#                      if all_even(dictionary)]
# print(result)

# Reflection: 

# Better to write readable code first, then optimize it. Terminate loops
# early if it no longer meets a condition etc. 
# LS solution breaks down solution into logical parts that each perform a specific 
# task and return a boolean. This makes it easier to understand and build the solution.


# Expected Result:
[{'e': [8], 'f': [6, 10]}]