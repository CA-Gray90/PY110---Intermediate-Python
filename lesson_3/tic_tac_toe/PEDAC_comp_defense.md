#### PEDAC - Computer defensive AI
# P 
Problem statement:
Make the computer defensive-minded so that, when an immediate threat exists, it
will try to defend the 3rd square. An immediate threat occurs when the human
player has 2 squares in a row with the 3rd square unoccupied. If there's no
immediate threat, the computer can pick a random square.

Inputs:
- board - i.e. dict containing moves that have been played

Outputs:
- board position (int) that is an immediate threat to the computer
- else None / False

RULES:
Explicit:
- An immediate threat is defined as the player has two squares in a row with
3rd unoccupied
- If no immediate threat exists, the computer can pick at random as normal

Implicit:
- player must have two in a 'row' but 2 out of 3 to win is also an immediate threat

Questions:

# E
None supplied, but given the following situation:
    e.g : X |   |  
         ---|---|---
          0 |   | 
         ---|---|---
            |   | X
    
    The computers next move should be:
    e.g : X |   |  
         ---|---|---
          0 | 0 | 
         ---|---|---
            |   | X  

or:
    e.g : X | X |  
         ---|---|---
          0 |   | 
         ---|---|---
            |   | 
    
    Computers next move:
    e.g : X | X | O
         ---|---|---
          0 |   | 
         ---|---|---
            |   |   

# D

# A
High Level:
1. After player has played thier move, check whether an `immediate threat` exists
2. If there is an `immediate threat`, computer plays that move
3. If not, computer plays a random move

# Checking an `immediate threat()`:
# PEDAC
# P
Given a list of winning combos, create a function that returns a move (number)
representing the immediate threat that exists to the computer, i.e the player
has 1 move left to win that game, else None

Input: 
- List of nested lists containing winning combos (3 numbers)
- the current board

Output: Winning move or None

# E
    WINNING_COMBOS = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # horizontal combos
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # vertical combos
        [1, 5, 9], [3, 5, 7]             # diagonal combos
    ]

    winning_move = next_winning_move(board)
    if winning_move:
        # Computer plays the move that is returned by this function
    else:
        # Computer picks a random move

# D

# A
1. LOOP through each nested list in WINNING_COMBOS:
2. IF board contains 2 out 3 squares as the human mark and the third as empty,
then return the remaining number (empty space)
    - assign sq1, sq2, sq3 to the nested combo
    - sq1 == human mark and sq2 == human mark and sq3 == empty space, 
        then return sq3
    etc for each possible combo
    
3. else return None