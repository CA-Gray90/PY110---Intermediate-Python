# What will the output be?

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# Output:
# {
# 'Fred' : 0,
# 'Barney' : 1,
# 'Wilma' : 2,
# 'Betty' : 3,
# 'Pebbles' : 4,
# 'Bambam' : 5
# }