# Determine the minimum age from the given dict.

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# PCODE:
# Use min(dict.values())

minimum_age = min(ages.values())
print(minimum_age) # --> 10