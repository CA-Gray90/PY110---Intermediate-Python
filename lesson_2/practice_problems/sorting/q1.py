# Sort the following list of numbers first in ascending numeric order, then in
# descending numeric order. Do not mutate the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst))
print(sorted(lst, reverse=True))
# Expected result:

# [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort