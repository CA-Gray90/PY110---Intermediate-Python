# Given the following data structure, sort the list so that the sub-lists are
# ordered based on the *sum* of the odd numbers that they contain.
# You shouldn't mutate the original list.
def sum_odds(lst):
    return sum([num for num in lst if num % 2 == 1])

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

sorted_lst = sorted(lst, key=sum_odds)

print(sorted_lst)
print(lst)
# Expected result:
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]