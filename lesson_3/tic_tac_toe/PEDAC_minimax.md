#### PEDAC - Minimax

# P
Problem Statement:
Create a function that returns the best next possible move in a game of tic tac
toe, no matter how many moves are left. 

Use the minimax game theory.

Inputs:
- Current moves available as a list of integers
- Current board

Outputs:
- best next position to play out of possible positions to play as an integer 1 - 9

RULES:
Explicit:
- Must return a single integer representing the next best move to play, or if
moves are equally good, one of them.
- Possible positions to play are 1 - 9

Questions:
- Do we need to use a recursive function to go down all possible routes and get 
all possible outcomes?
- Can we control depth and therefore control how accurate the next best move is? 
i.e. difficulty?
- How do we keep track of all the moves played??

# E
Simple Example:
         [X's Turn]         <you choose
         /       \
     Move A     Move B
     /   \        /   \
   [O]   [O]    [O]   [O]     <opponent's best responses
   / \    / \    / \   / \
 [+1][0][0][-1][-1][0][+1][-1] <game results (end of game)

# D
- a dict of all possible branches and outcomes? 
- outcomes are either +1 : win, 0 : draw, -1 : loss
- list of possible outcomes for each branch, summing up the outcomes to choose
highest scoring branch

# A:
High Level:
1. Using the list of possible moves to play, <get the best possible move> for the COMPUTER and <simulate playing that move>
2. If the game ends, <produce a score>: +1, 0, -1 depending on whether it is a win or draw or loss
 - 2.5 If a score is produced, add it to a list associated with the move first played in that trial run played
3. If the game doesn't end, <simulate the opponent playing a move> from the remaining moves to play
4. Repeat steps 1 to 3
5. When all possible branches have been explored, sum up the scores of each possible
branch
6. Compare the sums and return the move that has the highest score, or appears first if there
are scores with even sums

More detailed Breakdown:

1. Create a copy of the board to use for simulations
2. Create a copy of the list of moves to modify as we simulate games
3. create a dict that keeps score of each possible move played, as they are played:
    - move 1 : [possible_scores_here],

OUTER LOOP:
    Initialize an empty list of `moves_played`
    <Simulate a move>:
    4. Using the list of possible moves to play + `moves_played`, get the best next possible move for the Computer and simulate playing that move
    5. If the game ends, <produce a score>: +1, 0 depending on whether it is a win or draw
            - RETURN / EXIT
    6. If the game doesn't end, <simulate the opponent playing a move> from the best remaining moves to play
        - Do so by <alternating which player> is next to play in running the simulation
        - If the game ends <produce a score>: -1, or 0 for a loss (for the computer) or a draw
            - RETURN / EXIT
    7. If the game doesn't end here, add this move to the `moves_played` list, then call <simulate a move> again.
8. If the game ended on this trial run, pass the score to the appropriate branch in the dict
9. Modify the copied list of remaining moves to remove the move just played
10. Go back to 4.



#### Helper Functions:
# Simluate playing a move:
1. LOOP: for each move that is available to play:
    - play that move
    - update the copied board
    - update the copied available list of moves
    - IF there is a win, or draw:
    return 'game end'
    - ELSE return `None`

# Get best possible to play next:
1. We've already done this in our tic tac toe game:
- If a next move is a win, play that move
- If a next move is a loss, play that move
- If 5 is available, play that move
- Finally, pick a random move

# Produce a score:
Inputs: board_copy, player_mark 
Outputs corresponding score: 1, 0, -1

Depending on which player mark is given to the function, it produces the appropriate 
score.
i.e. If computer mark is entered, produces +1 if computer has won, -1 if player has won

# Alternate player mark
return human mark if computer mark, and vice versa


