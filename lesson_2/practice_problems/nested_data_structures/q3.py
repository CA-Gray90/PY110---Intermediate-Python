# Given the following code, what will the final values of a and b be?
# Try to answer without running the code.

a = 2
b = [5, 8]
lst = [a, b] # assign lst to a list containing the objects referenced by `a` and `b`

lst[0] += 2
lst[1][0] -= a

# Answer:
# a -> 2 
# b -> [3, 8]

print(lst)
print(a == 2)
print(b == [3, 8])