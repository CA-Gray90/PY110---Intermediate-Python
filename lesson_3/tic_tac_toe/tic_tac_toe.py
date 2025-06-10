import os       # Alphabetize imports
import random

EMPTY_SQUARE = ' ' # Avoid magic constants, use Symbolic Constants
HUMAN_MARK = 'X'
COMPUTER_MARK = 'O'
GAMES_TO_WIN_MATCH = 3
MIDDLE_SQUARE = 5
CORNER_SQUARES = [1, 3, 7, 9]
WINNING_COMBOS = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], # horizontal combos
    [1, 4, 7], [2, 5, 8], [3, 6, 9], # vertical combos
    [1, 5, 9], [3, 5, 7]             # diagonal combos
]

GOES_FIRST = 'choose'
GAME_TITLE = ' *** Ultimate Tic Tac Toe *** '
BOARD_SQUARE_POSITIONS = {num : num for num in range(1, 10)}

def clear_terminal():
    os.system('clear')

def display_game_title():
    print(GAME_TITLE)

def prompt(text):
    print(f'==> {text}')

def list_text(text):
    print(f' - {text}')

def display_welcome():
    print('Welcome to'.center(len(GAME_TITLE), ' '))
    print(GAME_TITLE)
    print()
    prompt('In this revolutionary game, '
           'you will pit yourself against a super intelligent AI player.\n'
           'Can you beat it?')
    print()

def display_rules():
    prompt('Would you like to see the rules? (y/n)')
    if yes_or_no():
        prompt('Here are the rules:')
        list_text('Each player gets a turn at putting a mark in a square on the board')
        list_text('The first player with 3 marks in a row, column or diagonal wins the game')
        print()
        list_text(f'First player to {GAMES_TO_WIN_MATCH} games will win the match')
        list_text('The match winner is the overall winner')
        print()
        list_text('When prompted to mark your square, you must enter a number that'
               ' corresponds to the square you intend to mark')
        print()
        list_text('The square positions are numbered as follows:')
        display_board(BOARD_SQUARE_POSITIONS)
        list_text('You will be prompted to choose who goes first and for a difficulty level')
        print()
        prompt('Now that you know the rules, you are ready to play!')
        enter_to_continue()

def choose_difficulty():
    prompt('Please choose the difficulty level for this match:\n'
           'Easy, Medium, Hard or Nightmare (e/m/h/n)')
    answer = input().strip().lower()
    while True:
        if answer in ['easy', 'medium', 'hard', 'nightmare', 'n', 'e', 'm', 'h']:
            if answer[0] == 'n':
                prompt('WARNING: NIGHTMARE MODE IS VIRTUALLY IMPOSSIBLE TO BEAT.')
                prompt('The creator of this game regrets unleashing such a'
                       ' powerful AI. Are you sure you wish to play this mode? (y/n)')
                if not yes_or_no():
                    prompt('Choose your difficulty level again (e/m/h/n):')
                    answer = input().strip().lower()
                else:
                    return answer[0]
            else:
                return answer[0]
        else:
            prompt('Oops, invalid input, please try again:')
            answer = input().strip().lower()
    
def display_difficulty_level(difficulty):
    match difficulty:
        case 'e':
            difficulty_level = 'Easy'
        case 'm':
            difficulty_level = 'Medium'
        case 'h':
            difficulty_level = 'Hard'
        case 'n':
            difficulty_level = 'Nightmare'
    prompt(f'{difficulty_level} difficulty mode')

def enter_to_continue():
    prompt('Press Enter to continue...')
    input()

def yes_or_no():
    answer = input().strip()
    while True:
        if answer.lower() in {'y', 'yes', 'n', 'no'}:
            return answer[0].lower() == 'y'
        else:
            prompt('Invalid input, please try again:')
            answer = input().strip()

def initialize_empty_board():
    return {num: EMPTY_SQUARE for num in range(1, 10)}

def display_board(board):
    print()
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('---|---|---')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('---|---|---')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print()

def display_ingame_board(board):
    print()
    prompt(f'Your mark is {HUMAN_MARK}. Computers mark is {COMPUTER_MARK}.')
    display_board(board)

def empty_squares(board):
    return [str(key) for key, value in board.items()
                     if value == EMPTY_SQUARE]

def initialize_empty_scorekeeper():
    return {'player' : 0, 'computer' : 0}

def display_scoreboard(scorekeeper):
    longer_name = max(scorekeeper.keys(), key=len)
    max_display_length = len(longer_name + ' : 0')

    print('+-' + '-' * max_display_length + '-+')
    print(f'|', 'SCOREBOARD'.center(max_display_length, ' '), '|')

    for player, score in scorekeeper.items():
        print('|', f'{player.capitalize()}'.ljust(len(longer_name)), ':', f'{score} |')

    print('+-' + '-' * max_display_length + '-+')

def join_or(lst, delimiter=', ', final_joiner='or'):
    lst_str = [str(num) for num in lst]

    if len(lst_str) > 2:
        result = [num + delimiter for num in lst_str[:-1]]
        result.extend([f'{final_joiner} ', lst_str[-1]])
        return ''.join(result)

    elif len(lst_str) == 2:
        return f'{lst_str[0]} {final_joiner} {lst_str[1]}'

    else:
        return ''.join(lst_str)

def player_turn(board):
    valid_choices = empty_squares(board)
    while True:
        prompt(f'Please choose a square to mark from the following choices:\n'
               f'({join_or(valid_choices)})')
        player_choice = input().strip()
        if player_choice in valid_choices:
            break

        prompt('Sorry, that was not a valid choice. Try again.')

    board[int(player_choice)] = HUMAN_MARK

def computer_turn(board, difficulty):
    empty_sqs = empty_squares(board)
        
    if empty_sqs:
        defensive_move = next_winning_move(board, HUMAN_MARK)
        offensive_move = next_winning_move(board, COMPUTER_MARK)
        
        easy_move = easy_difficulty_move(empty_sqs)
        medium_move = medium_add_on(defensive_move, offensive_move)
        hard_move = hard_add_on(empty_sqs)
        nightmare_add_on = nightmare_mode_add_on(empty_sqs)

        match difficulty:
            case 'n':
                for move in [medium_move, hard_move, nightmare_add_on, easy_move]:
                    if move:
                        choice = move
                        break
            case 'h':
                for move in [medium_move, hard_move, easy_move]:
                    if move:
                        choice = move
                        break
            case 'm':
                if medium_move:
                    choice = medium_move
                else:
                    choice = easy_move
            case 'e':
                choice = easy_move

        board[int(choice)] = COMPUTER_MARK

def easy_difficulty_move(empty_squares):
    return random.choice(empty_squares)

def medium_add_on(defensive_move, offensive_move):
    if offensive_move:
        return offensive_move
    elif defensive_move:
        return defensive_move
    return None

def hard_add_on(empty_squares):
    if '5' in empty_squares:
        return MIDDLE_SQUARE
    return None

def nightmare_mode_add_on(empty_squares):
    avail_corners = [sq for sq in CORNER_SQUARES if str(sq) in empty_squares]
    if avail_corners:
        return random.choice(avail_corners)
    return None

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

def update_scorekeeper(board, scorekeeper):
    winner = detect_winner(board)
    if winner:
        scorekeeper[winner] += 1

def next_winning_move(board, player_mark):
    for combo in WINNING_COMBOS:
        marks_in_line = [board[sq] for sq in combo]

        if marks_in_line.count(player_mark) == 2:
            for sq in combo:
                if board[sq] == EMPTY_SQUARE:
                    return sq
    return None

def get_match_winner(scorekeeper):
    for name in scorekeeper.keys():
        if scorekeeper[name] == GAMES_TO_WIN_MATCH:
            return name
    return None

def display_match_winner(match_winner):
    if match_winner == 'player':
        print()
        prompt('*** Congratulations! You won the match! ***')
        prompt("Looks like AI won't be coming for our jobs just yet!")
        print()
    elif match_winner == 'computer':
        print()
        prompt('*** You lost! ***')
        prompt('Unfortunately you have lost the match! Looks like AI'
        ' might be coming after our jobs after all...')
        print()

def who_goes_first():
    if GOES_FIRST == 'choose':
        prompt('Choose who will take the first turn in each game of this match:\n'
               "Enter either 'Player', 'Computer' or 'Random' (p/c/r):")
        answer = input().strip()
        while True:
            if answer.lower() in {'p', 'player', 'c', 'computer', 'r', 'random'}:
                match answer[0]:
                    case 'p':
                        return 'player'
                    case 'c':
                        return 'computer'
                    case 'r':
                        return random.choice(['player', 'computer'])
            else:
                prompt('Oops that was an invalid input, please try again:')
                answer = input().strip()
    else:
        return GOES_FIRST
    
def display_who_goes_first(goes_first):
    prompt(f'{goes_first.capitalize()} will go first.')

def choose_square(current_player, board, difficulty):
    match current_player:
        case 'player':
            player_turn(board)
        case 'computer':
            computer_turn(board, difficulty)

def alternate_player(current_player):
    match current_player:
        case 'player':
            return 'computer'
        case 'computer':
            return 'player'

def play_again():
    prompt('Would you like to play another match? (y/n)')
    answer = yes_or_no()
    return answer

def clear_and_display_game_info(board, scorekeeper):
    clear_terminal()
    display_game_title()

    display_scoreboard(scorekeeper)
    display_ingame_board(board)

def play_game(goes_first, scorekeeper, difficulty):
    while True:
        board = initialize_empty_board()
        current_player = goes_first

        while True:
            clear_and_display_game_info(board, scorekeeper)

            choose_square(current_player, board, difficulty)
            current_player = alternate_player(current_player)
            if board_full(board) or winning_board(board):
                break

        update_scorekeeper(board, scorekeeper)
        clear_and_display_game_info(board, scorekeeper)

        if winning_board(board):
            prompt(f'{detect_winner(board).capitalize()} won the game!')
        else:
            prompt("It's a tie!")
        
        if get_match_winner(scorekeeper):
            break

        prompt('Are you ready for the next game? (y/n)')
        if not yes_or_no():
            break

# Main Program:
def main():
    clear_terminal()
    display_welcome()
    display_rules()

    while True:
        scorekeeper = initialize_empty_scorekeeper()
        difficulty = choose_difficulty()
        goes_first = who_goes_first()

        display_who_goes_first(goes_first)
        display_difficulty_level(difficulty)
        enter_to_continue()

        play_game(goes_first, scorekeeper, difficulty)
        match_winner = get_match_winner(scorekeeper)
        display_match_winner(match_winner)

        if not play_again():
            break

    prompt('Thank you for playing! Goodbye.')

main()

# TODO:
# Add timing pauses to make game feel more interactive
#   - slower pauses in easy mode
#   - shorter pauses for each subsequent difficulty mode?
# Pylint
# Any refactoring?