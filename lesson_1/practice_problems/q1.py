# How would you count the number of occurances of the word 'banana' in the given
# tuple?

fruits = ("apple", "banana", "cherry", "date", "banana")

# Solutions:

print(fruits.count('banana')) # --> 2

# Set a counter variable to zero, iterate through the given list, compare each
# element to the value we wish to count, and increment `counter` each time we find 
# a match

def find_thing(lst, thing):
    counter = 0
    for item in lst:
        if item == thing:
            counter += 1
    
    return counter

print(find_thing(fruits, 'banana')) # --> 2