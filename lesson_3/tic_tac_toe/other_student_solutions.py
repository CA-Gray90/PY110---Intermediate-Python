# Notes on program design:
#
# You can configure the game to prompt the player to choose which side
# they want to play and/or whether they play first. See constants below.
#
# The board is an array of cells using the following indexes:
#
# 0 1 2
# 3 4 5
# 6 7 8
#
# In the board array, positions are marked by 'h', 'c', or None
# ('h' and 'c' are constants HUMAN and COMPUTER, respectively).
#
# sample board: [None, 'h', None, None, None, 'c', 'c', None, 'h']
#
# The human player is asked to identify cells by spreadsheet notation,
# which is then translated to the internal indexed representation.
#
# We represent player order and side assignment using a 'config'
# data structure like this:
# [{'player': COMPUTER, 'side': O_SIDE, 'pp': 'Computer'},
#  {'player': HUMAN, 'side': X_SIDE, 'pp': 'Human'}]
# This conveys that computer plays first and is playing O.
#
# When we print the board, for a given cell we have to first match up
# the player identifier (HUMAN or COMPUTER) with the side assigned at
# game start (X_SIDE or O_SIDE) and then use the appropriate pretty
# print string for the assigned side (X_PP vs O_PP). The pretty print
# strings are 5 rows by 11 columns and were created with the python
# ascii art module.
#
# TODO:
# - if configured to prompt for x/y, going first or not etc., do it per
#   match, not per program run.

import random
import os

HUMAN = 'h'
COMPUTER = 'c'

X_SIDE = 'X'
O_SIDE = 'O'

CHOOSE = 'choose'

## -------------------------------------------------
# Config for gameplay options -- you may edit these
HUMAN_SIDE = X_SIDE # or O_SIDE or CHOOSE
PLAYS_FIRST = HUMAN # or COMPUTER or CHOOSE
## -------------------------------------------------

CENTER_CELL = 4

# This provides a mapping of spreadsheet notation identifiers to the
# internal board list indices. It also serves for input validation.
VALID_CELLS = [row + col
               for col in ['1', '2', '3']
               for row in ['A', 'B', 'C']]

# These are the sets of cells that can win the game if they contain
# all three of the same marker.
WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
    [0, 4, 8], [2, 4, 6]             # diagonals
    ]


X_PP = [l.ljust(11) for l in """
8b,     ,d8
 `Y8, ,8P'
   )888(
 ,d8" "8b,
8P'     `Y8
""".strip('\n').split('\n')]

O_PP = [l.ljust(11) for l in """
 ,adPPYba,
a8"     "8a
8b       d8
"8a,   ,a8"
 `"YbbdP"'
""".strip('\n').split('\n')]


def get_yn_choice(prompt):
    while True:
        response = input(prompt + " (y/n) ")
        try:
            return bool(['n', 'y'].index(response[:1].lower()))
        except ValueError:
            print(f"Invalid value '{response}', try again.")

def get_config(config, player_id, prop_name=None):
    for c in config:
        if c['player'] == player_id:
            if prop_name is None:
                return c
            if prop_name in c:
                return c[prop_name]
            raise ValueError(f"Prop {prop_name} not found for player {player_id}.")
    raise ValueError(f"Player {player_id} not found.")


def print_board(b, c):

    def get_pp_row(player_id, config, row_index):
        side = get_config(config, player_id, 'side')
        return X_PP[row_index] if side == X_SIDE else O_PP[row_index]

    def cell_row(board, config, cell, row):
        result = ''
        if board[cell] is None:
            result += ' ' * 11
        else:
            result += get_pp_row(board[cell], config, row)
        return result

    os.system('clear')
    print('  ' + (' ' * 5) + 'A' + (' ' * 5) + '   ' + (' ' * 5) + 'B' + (' ' * 5) + '   ' + (' ' * 5) + 'C')
    print('  ' + (' ' * 11) + ' | ' + (' ' * 11) + ' |')
    print('  ' + cell_row(b, c, cell=0, row=0) + ' | ' + cell_row(b, c, cell=1, row=0) + ' | ' + cell_row(b, c, cell=2, row=0))
    print('  ' + cell_row(b, c, cell=0, row=1) + ' | ' + cell_row(b, c, cell=1, row=1) + ' | ' + cell_row(b, c, cell=2, row=1))
    print('1 ' + cell_row(b, c, cell=0, row=2) + ' | ' + cell_row(b, c, cell=1, row=2) + ' | ' + cell_row(b, c, cell=2, row=2))
    print('  ' + cell_row(b, c, cell=0, row=3) + ' | ' + cell_row(b, c, cell=1, row=3) + ' | ' + cell_row(b, c, cell=2, row=3))
    print('  ' + cell_row(b, c, cell=0, row=4) + ' | ' + cell_row(b, c, cell=1, row=4) + ' | ' + cell_row(b, c, cell=2, row=4))
    print('  ' + (' ' * 11) + ' | ' + (' ' * 11) + ' |')
    print('  ' + ('-' * 11) + '-+-' + ('-' * 11) + '-|-' + ('-' * 11) + '-')
    print('  ' + (' ' * 11) + ' | ' + (' ' * 11) + ' |')
    print('  ' + cell_row(b, c, cell=3, row=0) + ' | ' + cell_row(b, c, cell=4, row=0) + ' | ' + cell_row(b, c, cell=5, row=0))
    print('  ' + cell_row(b, c, cell=3, row=1) + ' | ' + cell_row(b, c, cell=4, row=1) + ' | ' + cell_row(b, c, cell=5, row=1))
    print('2 ' + cell_row(b, c, cell=3, row=2) + ' | ' + cell_row(b, c, cell=4, row=2) + ' | ' + cell_row(b, c, cell=5, row=2))
    print('  ' + cell_row(b, c, cell=3, row=3) + ' | ' + cell_row(b, c, cell=4, row=3) + ' | ' + cell_row(b, c, cell=5, row=3))
    print('  ' + cell_row(b, c, cell=3, row=4) + ' | ' + cell_row(b, c, cell=4, row=4) + ' | ' + cell_row(b, c, cell=5, row=4))
    print('  ' + (' ' * 11) + ' | ' + (' ' * 11) + ' |')
    print('  ' + ('-' * 11) + '-+-' + ('-' * 11) + '-|-' + ('-' * 11) + '-')
    print('  ' + (' ' * 11) + ' | ' + (' ' * 11) + ' |')
    print('  ' + cell_row(b, c, cell=6, row=0) + ' | ' + cell_row(b, c, cell=7, row=0) + ' | ' + cell_row(b, c, cell=8, row=0))
    print('  ' + cell_row(b, c, cell=6, row=1) + ' | ' + cell_row(b, c, cell=7, row=1) + ' | ' + cell_row(b, c, cell=8, row=1))
    print('3 ' + cell_row(b, c, cell=6, row=2) + ' | ' + cell_row(b, c, cell=7, row=2) + ' | ' + cell_row(b, c, cell=8, row=2))
    print('  ' + cell_row(b, c, cell=6, row=3) + ' | ' + cell_row(b, c, cell=7, row=3) + ' | ' + cell_row(b, c, cell=8, row=3))
    print('  ' + cell_row(b, c, cell=6, row=4) + ' | ' + cell_row(b, c, cell=7, row=4) + ' | ' + cell_row(b, c, cell=8, row=4))
    print('  ' + (' ' * 11) + ' | ' + (' ' * 11) + ' |')
    #print("Remaining choices", remaining_choices(b))

def initialize_board():
    return [None for _ in range(0,9)]

def set_cell(board, cell, player_id):
    if player_id not in [HUMAN, COMPUTER]:
        raise ValueError(f"Player must be {HUMAN} or {COMPUTER}; {player_id} given.")
    if not isinstance(cell, int) or len(board) > cell < 0:
        raise ValueError(f"Cell index not an int within the board range: {cell}")
    board[cell] = player_id

def remaining_choices(board):
    return [i for i, mark in enumerate(board) if mark is None]

def find_completable_line(board, player_id):
    if player_id not in [HUMAN, COMPUTER]:
        raise ValueError("Not a valid player identifier: " + player_id)
    for combo in WINNING_COMBOS:
        line = [board[cell] for cell in combo]
        if line.count(player_id) == 2 and line.count(None) == 1:
            return combo[line.index(None)]
    return None

def humans_turn(board):
    remaining = remaining_choices(board)
    while True:
        if len(remaining) == 1:
            # Skip the question to the player, there's only one choice
            selection_index = remaining[0]
        else:
            selection = input("Choose a cell using spreadsheet notation e.g. C2: ").strip().upper()
            if selection not in VALID_CELLS:
                print("Invalid choice, try again.")
                continue
            selection_index = VALID_CELLS.index(selection)
            if board[selection_index] is not None:
                print("Cell is already taken, try again.")
                continue
        set_cell(board, selection_index, HUMAN)
        break

def computers_turn(board):
    # offense, then defense
    # BUGBUG: zero is treated like None in the following
    # choice = find_completable_line(board, COMPUTER) or \
    #     find_completable_line(board, HUMAN)
    choice = find_completable_line(board, COMPUTER)
    if choice is None:
        choice = find_completable_line(board, HUMAN)

    # if the center square is available, take it
    if choice is None and 4 in remaining_choices(board):
        choice = CENTER_CELL

    # TODO: place in a square adjacent to a previous move, if possible

    # Fallback: random
    if choice is None:
        choice = random.choice(remaining_choices(board))

    set_cell(board, choice, COMPUTER)

def winner(board):
    for combo in WINNING_COMBOS:
        sq1, sq2, sq3 = combo
        if board[sq1] == board[sq2] == board[sq3] and board[sq1]:
            return board[sq1]
    return None

def play_game(config):
    board = initialize_board()
    turn_number = -1
    try:
        while True:
            print_board(board, config)

            turn_number += 1
            current_player = config[turn_number % len(config)]
            if current_player['player'] == HUMAN:
                humans_turn(board)
            else:
                computers_turn(board)

            maybe_winner = winner(board)
            if maybe_winner:
                print_board(board, config)
                print("Winner: " + get_config(config, maybe_winner, 'pp'))
                return maybe_winner
            if len(remaining_choices(board)) == 0:
                print_board(board, config)
                print("Board full - Tie.")
                return None
    finally:
        print(f"Game ended after {turn_number + 1} turns.")

def main_loop():
    def get_player_order_choice():
        if get_yn_choice("Do you want to play first?"):
            return HUMAN
        return COMPUTER

    def get_human_side_choice():
        if get_yn_choice("Do you want to be 'x'?"):
            return X_SIDE
        return O_SIDE

    print("Welcome to TTT.")

    # First determine which player is which side
    human_side = get_human_side_choice() if HUMAN_SIDE == 'choose' else HUMAN_SIDE

    # Next work out playing order
    plays_first = get_player_order_choice() if PLAYS_FIRST == 'choose' else PLAYS_FIRST

    # Set up the configs
    config = [{'player': HUMAN, 'pp': 'Human', 'side': human_side, 'score': 0}]
    insert_computer_at = 0 if plays_first == COMPUTER else 1
    config.insert(insert_computer_at,
                  {'player': COMPUTER,
                   'pp': 'Computer',
                   'side': O_SIDE if human_side == X_SIDE else X_SIDE,
                   'score': 0})

    # Report out who is playing which side and who plays first.
    print(" ".join([p['pp'] + ' is ' + p['side'] + '.' for p in config]))
    print(f"{config[0]['pp']} plays first.")

    num_games = 0
    while True:
        num_games += 1
        winner_of_game = play_game(config)

        if winner_of_game is not None:
            winning_player = get_config(config, winner_of_game)
            winning_player['score'] += 1

        # Sort descending by score to identify the winner.
        # Must make a copy here, mutating config would change player order.
        leaderboard = sorted(config, key=lambda x: x['score'], reverse=True)

        print("Current match score: " + \
              ', '.join([f'{p["pp"]} {p["score"]}' for p in leaderboard]) + \
              f" after {num_games} game(s).")

        # Compare score of first two entries to determine winner.
        if num_games >= 2 and leaderboard[0]['score'] > leaderboard[1]['score']:
            print(f"{leaderboard[0]['pp']} wins the match!!")
            # Reset the scores and match game count
            num_games = 0
            for c in config:
                c['score'] = 0

        if not get_yn_choice("Do you want to play again?"):
            break
    print("Goodbye!")

main_loop()