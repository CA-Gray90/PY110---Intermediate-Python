# Calculate the total age given the following dictionary:

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# PCODE:
# set a counter variable.
# Iterate through the dict values
# Add the current value to the counter variable on each iteration
# return the counter variable

total_age = 0
for age in ages.values():
    total_age += age
    
print(total_age)

# Or use 'sum()' passing in the dict.values() view object

total_age = sum(ages.values())
print(total_age)