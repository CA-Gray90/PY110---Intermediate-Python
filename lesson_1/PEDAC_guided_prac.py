'''
Algorithm:
    High Level:
    - Build each layer of the structure with the number of blocks till you 
    can't build a valid layer
    - calculate the left over blocks after building the structure and return it

    Detailed: 
    - Get a starting_blocks number (number of blocks to build "structure")
    - SET remainder_blocks to value of starting_blocks
    - SET a `current_layer` variable to 1 (layer 1)
    - SET a `layer_blocks` variable to number of layer_blocks required for current
    `current_layer`:
        - layer_blocks = `current_layer` squared
    - LOOP:
        IF `layer_blocks` is less than remainder_blocks:
            - decrement starting_blocks by value of `layer_blocks`
            - incremenet `current_layer` by 1
        - ELSE:
            - break out of loop
    
    - return the value of remainder_blocks 
'''

def calculate_leftover_blocks(starting_blocks):
    remainder_blocks = starting_blocks
    current_layer, current_layer_blocks = 1, 1

    while remainder_blocks >= current_layer_blocks:
        remainder_blocks -= current_layer_blocks
        current_layer += 1
        current_layer_blocks = current_layer ** 2
    
    return remainder_blocks

# Test Cases:

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True