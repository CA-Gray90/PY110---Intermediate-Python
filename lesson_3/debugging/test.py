import pdb

def test():
    print("Inside the function!")

print("Before function call")
pdb.set_trace()
test()
print("After function call")