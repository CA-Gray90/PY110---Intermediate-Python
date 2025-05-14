# Given the following data structure, return a new list with the same structure
# but with the values in each sublist ordered in ascending order. Use a
# comprehension if you can. (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
ordered_lst = []

# For loop:
for item in lst:
    ordered_lst.append(sorted(item))

print(ordered_lst == [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']])

# Comprehension:
ordered_lst = [sorted(sublist) for sublist in lst]

print(ordered_lst == [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']])

# Expected Result:
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]