#### PEDAC - Difficulty setting
# P
Problem statement:
Add a difficult setting in our tic tac toe game.

Give the player 3 choices; easy, medium, hard, (impossible? minimax...?)

Easy - computer always chooses at random and does not attempt to block the
player if they get close to winning. If the computer is about to win, they will
play the winning move

Medium - Computer will block the player from winning and will play its own winning
move if present. 

Hard - Computer will:
- block player from winning if next win present
- play winning move if about to win
- play 5 if 5 is empty
- if 5 has been played, it will play a corner square if no threats exist.
It won't be a perfect system but this should make it harder for the player to
win, mostly likely will keep being a draw. 

# E

# D

# A
1. Player is prompted at beginning of match to choose a difficulty setting
2. Difficulty setting determines which algorithm computer player will use
3. Add the end of the match, if player wants to play again, they can choose difficulty

1. 
- Create a function that provides the user with the choice of difficulty:
    - Easy, 'e'
    - Medium, 'm'
    - Hard, 'h'
- Assign the outcome to a variable named `difficulty_setting`

2.
- Modify the computers turn to determine which algorithm it will use to play the game
    - Divide up the algorithm into three functions:
        - Easy = random choice
        - Medium = take wins -> block threats 
                                    -> random choice (easy algorithm)
        - Hard = (Medium algorithm) 
                            -> take 5 -> take corners 
                                                -> (easy algorithm)

