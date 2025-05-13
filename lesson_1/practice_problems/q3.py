# How would you get the unique members from both sets?

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Use the union method or operator: .union(), '|'. This returns a new set.

unique_mems = a.union(b)
# Or:
# unique_mems = a | b
print(unique_mems)