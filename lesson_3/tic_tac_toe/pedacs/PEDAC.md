#### PEDAC - TIC TAC TOE

### HIGH-LEVEL:
# Problem description:
We want to create a 1 player TTT game in which a user plays against the computer

# Game description:
Tic-tac-toe (TTT) is a 2 player game that is played on a 3x3 board in which each player
takes turns to put a mark on the board.
A player wins when they get 3 marks in a row -
    either horizontally, vertically or diagonally
If the board is full and no player has won, then it is a tie.

# Program flow (High-Level):
0. Initialize an empty scoreboard
1. Display an initial empty board
1.5 Display the scoreboard
1.6 Ask the user who goes first, player, computer, or random.
2. Ask the user to mark a position
3. Computer marks a position
4. Update the board and display it
5. If there is a winner - display the winner AND
6. If the board is full - display its a tie
7. If there is no winner, go to step 2.
8. If it is a tie/ or there was a winner:
    - Update the scores and display the scoreboard. If it is a tie, no player gets a score
    - ask if player wants to `(play again)` - Continue playing the current match or quit early?
9. If player wants to continue, go to step 1
9.1    - If there is match winner, display the match winner
9.2    - Ask if the user wishes to play another match
9.3    - If the user wants to continue, go to step 0
10. If player doesnt want to play, quit the program

Three main loops:
    - 1. Outer loop: Steps 1 - 10
    - 1. Next inner loop: Step 1 - 9
    - 2. Inner loop: Steps 2 - 7

## PEDAC for High-Level Program flow steps:
# STEP 1 - PEDAC:
# P 
Display an initial empty board:
# E

# D
How do we display the board using python data structures?
- Using nested lists? Matrix?
- Choose a data structue based on the needs of the future program:
    - We will need to use it to get a winner, checking horizontal, vertical and 
    diagonal squares
- Using a dict with square numbers 1 - 9 and associated values:
    - 1 would be topleft
    - 2 : top middle
    - 3 : top right
    - 4 : left middle
    - ...

    e.g : 1 | 2 | 3
         ---|---|---
          4 | 5 | 6
         ---|---|---
          7 | 8 | 9

    board = {
        1 : 'X',
        2 : ' ',
        3 : ' ',
        4 : ' ',
        5 : 'O',
        6 : ' ',
        7 : ' ',
        8 : ' ',
        9 : 'X'
    }

    The above should display the board like:
    e.g : X |   |  
         ---|---|---
            | O | 
         ---|---|---
            |   | X

    - Using dict key access syntax to display the appropriate value for each
    empty space in the display dict

# A
 - Create an empty board that we display
 - Create a dict that will contain data to pass to the empty board

# C

## Step 2 - PEDAC
# P
Ask the user to mark a position, computer marks a position

- What are the valid choices? Co-ordinates? Numbers 1 - 9?
- Validate input:
    - Has the move been played before? By the user or computer?
    - Is the input a valid option?

- Update the board dictionary with the correct move
- Will the user be 'X' or 'O'?

- Computer chooses a move
- Random choice between 1 - 9?
- Is the choice valid? I.e Has the move been played before?
    - Check against the board dictionary
- Update the board dictionary with the computers move

## Step 5: Determining if there is a winner
# P:
Determining if there is a winner:
Input: board dictionary
Output: Boolean representing whether there is a winner (True or False)

RULES:
Explicit:
- A winning board is defined by 3 marks in a row, either:
    - horizontally
    - vertically
    - diagonally

Implicit:
- There are 3 possible horizontal winning combos
- There are 3 possible vertical winning combos
- There are 2 possible diagonal winning combos
- In TOTAL there are 8 possible winning combinations

Questions:

# E:
Examples of winning boards:
Horizontal:
e.g : X | X | X
     ---|---|---
        |   | 
     ---|---|---
        |   | 

Vertical:
e.g : X |   |  
     ---|---|---
      X |   | 
     ---|---|---
      X |   | 

Diagonal:
e.g : X |   |  
     ---|---|---
        | X | 
     ---|---|---
        |   | X

# Data Structure
- Winning combos dictionary to check against?

# Algorithm
- 1. SET a dictionary of all possible winning combinations based on board
positions
- 2. After each player (and computer) turn, check the board for any winning
combinations

e.g: horizontal winning combos : [1, 2, 3], [4, 5, 6], [7, 8, 9]

      X | X | X
     ---|---|---
        |   | 
     ---|---|---
        |   | 
    
    if we don't have a space (EMPTY_SQUARE) in any of the horizontal combo elements,
    we have a winning board.

    ' ' not in [1, 2, 3] = True --> we have a winner

    Other possibility:
    Iterate through each winning combo, if each value == PLAYER_MARK or COMPUTER_MARK:
        We have a winner