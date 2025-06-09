#### PEDAC - Keep Score functionality
# P 
Problem Statement:
Keep track of how many times the player and computer each win, and report the
scores after each game. The first player to win 5 games wins the overall match
(a series of 2 or more games). The score should reset to 0 for each player when
beginning a new match. Don't use any global variables. However, you may want to
use a global constant to represent the number of games needed to win the match.

Inputs:
- Scores - player wins and computer wins

Outputs:
- Tally of scores for the both the player and computer after each game
- First player to win the match (5 game wins)

RULES:
Explicit:
- Dont use any global variables
- report scores after each game.
- 5 game wins equals a match win
- scores should reset to 0 after a match is won
- use a global constant to represent how many games needed to win a match

Implicit:

Questions:
- What is meant by 2 or more games to win an overall match?
- Don't use any global variables, so everything must be contained within a function?
- One function that does everything or divide it up into a couple of functions?

# E
None given...

# Data Structure:
- Dictionary for keeping track of player score and computer score
- Perhaps a helper function to reset the scores
- A function to display the scores after each game?
- A Constant to represent games needed to win in order to win a match

# Algorithm

# C

### PEDAC - display scoreboard
# P
Problem Statement:
create a function that takes a dictionary as argument with two keys; a player
and computer and scores as values. Display the player name and computer name 
with thier scores in a box created by characters '-' and '|'

# E
+--------------+
| Player   : 0 |
| Computer : 0 |
+--------------+

# D

# A 
1. Get the max length of the display
2. Print the first line using the max length of the display
3. Print out the player + score
4. print out the computer name + score
5. print out the final line of dashes etc

#### PEDAC