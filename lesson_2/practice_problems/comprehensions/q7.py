# Given the following data structure return a new list identical in structure
# to the original, but containing only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# new_lst = []
# new_sublists = []

# for sublist in lst:
#     for num in sublist:
#         if num % 3 == 0:
#             new_sublists.append(num)
#     new_lst.append(new_sublists)
#     new_sublists = []

# Comprehension:
# Too much refactoring...?

new_lst = [[num for num in sublist if num % 3 == 0]
           for sublist in lst]

# Outsourcing to function:
def get_odds(lst):
    return [num for num in lst if num % 3 == 0]

new_lst = [get_odds(sublist) for sublist in lst]

print(new_lst == [[], [3, 12], [9], [15, 18]])

# Expected output:
# [[], [3, 12], [9], [15, 18]]