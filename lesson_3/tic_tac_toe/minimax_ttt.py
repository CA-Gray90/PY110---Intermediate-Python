import random

EMPTY_SQUARE = ' '
HUMAN_MARK = 'X'
COMPUTER_MARK = 'O'
GAMES_TO_WIN_MATCH = 3

WINNING_COMBOS = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], # horizontal combos
    [1, 4, 7], [2, 5, 8], [3, 6, 9], # vertical combos
    [1, 5, 9], [3, 5, 7]             # diagonal combos
]

def initialize_empty_board():
    return {num: EMPTY_SQUARE for num in range(1, 10)}

def display_board(board):
    # print()
    # prompt(f'Your mark is {HUMAN_MARK}. Computers mark is {COMPUTER_MARK}.')
    print()
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('---|---|---')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print()

def empty_squares(board):
    return [str(key) for key, value in board.items()
                     if value == EMPTY_SQUARE]

def board_full(board):
    return empty_squares(board) == []

def winning_board(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for combo in WINNING_COMBOS:
        sq1, sq2, sq3 = combo
        if board[sq1] == HUMAN_MARK\
                and board[sq2] == HUMAN_MARK\
                and board[sq3] == HUMAN_MARK:
            return 'player'
        elif board[sq1] == COMPUTER_MARK\
                and board[sq2] == COMPUTER_MARK\
                and board[sq3] == COMPUTER_MARK:
            return 'computer'
        
    return None

def next_winning_move(board, player_mark):
    for combo in WINNING_COMBOS:
        marks_in_line = [board[sq] for sq in combo]

        if marks_in_line.count(player_mark) == 2:
            for sq in combo:
                if board[sq] == EMPTY_SQUARE:
                    return sq
    return None

# Simulating a trial move:
def play_trial_move(board_copy, move, player_mark):
    board_copy[move] = player_mark # Mutates the copied board through reference
    if winning_board(board_copy) or board_full(board_copy):
        return 'game_end'
    return None

# Getting the next best possible move:
def get_next_best_move(board, player_mark, played_moves):
    empty_sqs = empty_squares(board)
    empty_sqs.extend(played_moves)

    offensive_move = next_winning_move(board, player_mark)
    deffensive_move = next_winning_move(board, alternate_player_mark(player_mark))

    if offensive_move:
        return int(offensive_move)
    elif deffensive_move:
        return int(deffensive_move)
    if '5' in empty_sqs:
        return 5
    return int(random.choice(empty_sqs))

# Getting a score (player will always be assumed to be 'computer' in this case):
def get_payoff_score(board_copy, player):
    ''' The payoff scores; +1, 0, or -1 will be returned as appropriate
    to the player passed as 2nd argument. 
    E.g: if player argument is 'computer', a win for the player will return -1,
    whereas a win for the computer will return 1
    '''

    winner = detect_winner(board_copy)
    if winner:
        return 1 if winner == player else -1
    return 0

# Alternate player mark for next move in simulation:
def alternate_player_mark(current_mark):
    if current_mark == HUMAN_MARK:
        return COMPUTER_MARK
    return HUMAN_MARK

# Simulate two moves:
def simulate_move(board_copy, current_player_mark, played_moves, branch_dict, initial_trial_move):
    original_board = board_copy.copy()
    current_player_mark = alternate_player_mark(current_player_mark)
    while True:
        # Swapping marks to then simulate the player move:

        # Getting the next best move to play for the computer and simulating it:
        next_best_move = get_next_best_move(board_copy, current_player_mark, played_moves)
        print(next_best_move)
        trial_run = play_trial_move(board_copy, next_best_move, current_player_mark)

        display_board(board_copy)

        board_copy[next_best_move] = current_player_mark
        print(board_copy)
        print(played_moves)

        if trial_run:
            payoff = get_payoff_score(board_copy, 'computer')
            branch_dict[f'Branch {initial_trial_move}'].append(payoff)
            played_moves.append(next_best_move)
            break
        else:
            print('Calling simulate move again')
            played_moves.append(next_best_move)
            simulate_move(board_copy, current_player_mark, played_moves, branch_dict, initial_trial_move)
            print('Exiting recursion')
            board_copy = original_board

board = initialize_empty_board() 

# Example board:
#      | X | 
#   ---+---+---
#    O | O | X
#   ---+---+---
#      | X |

# board[1] = 'O'
board[2] = 'X'
# board[3] = ' '
board[4] = 'O'
board[5] = 'O'
board[6] = 'X'
# board[7] = 'O'
board[8] = 'X'
# board[9] = ' '

print('Start simulation')
print('Original board:')
display_board(board)
copied_board = board.copy()
moves_played = []
possible_branches = {}

current_player_mark = COMPUTER_MARK
# Playing the first initial move
initial_trial_move = 1
print(f'Trial move: {initial_trial_move}')
possible_branches[f'Branch {initial_trial_move}'] = []
play_trial_move(copied_board, initial_trial_move, current_player_mark)

display_board(copied_board)

# simulating the possible outcomes from playing the initial move
simulate_move(copied_board, current_player_mark, moves_played, possible_branches, initial_trial_move)
# Looping through to get to an end:
# while True:
#     # Getting the next best move to play for the computer and simulating it:
#     # Swapping marks to then simulate the player move:
#     current_player_mark = alternate_player_mark(current_player_mark)

#     next_best_move = get_next_best_move(copied_board, current_player_mark)
#     print(f'The next best move for {current_player_mark} is: {next_best_move}')
#     trial_run = play_trial_move(copied_board, next_best_move, current_player_mark)

#     display_board(copied_board)

#     if trial_run:
#         print(f'Trial ended in a: {trial_run}')
#         payoff = get_payoff_score(copied_board, 'computer')
#         print(f'Payoff score of trial run: {payoff}')
#         possible_branches[f'Branch {initial_trial_move}'].append(payoff)
#         break
#     else:
#         print('no payoff for this run')



print(possible_branches[f'Branch {initial_trial_move}'])
print('Trial ended')

print('Original board:')
display_board(board)