import random
import os
import time
import pdb

BEST_OF = 3
BLACKJACK = 21
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']
CARDS_PER_HAND = 2
COURT_CARD_VALUE = 10
DEALER_STAY = 17
PLAYERS = 1
SUITES = ['diamonds', 'clubs', 'hearts', 'spades']
GAME_TITLE = '*' * 10 + ' TWENTY ONE ' + '*' * 10

def prompt(message):
    print(f'=> {message}')

def clear_terminal():
    os.system('clear')

def get_valid_input(*valid_answers):
    '''
    You can pass any number of arguments as 'valid answers' to check against.
    'valid answers' must be lower case.
    Returns the valid answer as entered.
    '''
    while True:
        answer = input().strip()
        if answer.lower() in valid_answers:
            return answer
        print("Oops, that isn't a valid answer, try again:")

def display_game_title():
    print(GAME_TITLE)

def display_welcome():
    print('Welcome to:'.center(len(GAME_TITLE), ' '))
    display_game_title()
    print()
    prompt('This is a game similar to the Casino game Blackjack but with a few'
           ' simplifications.')

def see_rules():
    prompt('Would you like to see the rule set? (y/n)')
    answer = get_valid_input('y', 'yes', 'no', 'n')
    return answer[0] == 'y'

def display_rules():
    def lst_txt(text):
        print(f'- {text}')
        print()
    print('*' * len(GAME_TITLE))
    prompt('RULES:\n(Assuming the User has some basic knowledge of'
           ' Blackjack and the value of the cards):')
    print()
    lst_txt(f'In this card game, you are attempting to get a total value as' 
            f' close to {BLACKJACK} as possible without going over.')
    lst_txt(f'If either the Player or Dealer gets {BLACKJACK} with thier first two'
            ' cards, it is an immediate win (Natural Blackjack).')
    lst_txt(f"If the Player gets to {BLACKJACK}, it is an automatic 'Stay'.")
    lst_txt(f"A total over {BLACKJACK} is a 'Bust'")
    lst_txt('Once it is the Dealers turn, thier 2nd card will be revealed.')
    lst_txt("The Dealer must 'Hit' till thier total is equal to or greater than"
            f' {DEALER_STAY}.')
    lst_txt("Equal total values equals a 'Draw'.")
    lst_txt(f'The overall winner is best out of {BEST_OF}.')
    print()
    print('*' * len(GAME_TITLE))

def enter_to_continue():
    prompt('Press Enter to continue...')
    input()

# Initialize empty deck:    
def initialize_deck():
    deck = []
    for suite in SUITES:
        for card in CARDS:
            deck.append({'card' : card, 'suite': suite})
    
    return deck

# Initialize game data structure:
def initialize_game_data_structure(deck, players=1):
    '''
    2nd argument is for number of players in game. Minimum 1 player.
    '''
    player_hands = {f'player{num}' : [] for num in range(1, players + 1)}

    return {
        'deck' : deck,
        'player_hands' : player_hands | {'dealer' : []}
    }

# Initialize dict where game results are kept track:
def initialize_game_results_dict(game_data):
    return {player : 0 for player in game_data['player_hands']}

# Shuffling a deck of cards:
def shuffle(deck):
    random.shuffle(deck)

# Deal players hands:
## Deal one card out (mutating)
def deal_card(deck):
    return deck.pop(0)

## Deal out hand:
def deal_hands(game_data):
    '''
    Deals each player two cards, one at a time as per real game.
    '''
    deck = game_data['deck']

    for _ in range(CARDS_PER_HAND):
        for player in game_data['player_hands']:
            game_data['player_hands'][player].append(deal_card(deck))

def get_hand(player, game_data):
    return game_data['player_hands'][player]

# Calculating hand with aces:
## Calculating aces:
def calc_ace(hand_total):
    '''
    Aces are worth 1 or 11 depending on context
    '''
    return 1 if hand_total >= 11 else 11

## Get hand total
def hand_total(hand):
    total = 0
    aces = 0

    for card_dict in hand:
        value = card_dict['card']
        if value != 'A':
            total += int(value) if value.isdigit() else COURT_CARD_VALUE
        else:
            aces += 1

    for _ in range(aces):
        total += calc_ace(total)

    return total

# Check for busted:
def busted(hand):
    return hand_total(hand) > BLACKJACK

# Check for blackjacks:
def is_blackjack(hand):
    '''
    Blackjack only happens when the player's first two cards equal 21.
    Automatic win.
    '''
    return hand_total(hand) == BLACKJACK and len(hand) == CARDS_PER_HAND

def check_for_blackjack(game_data):
    '''
    Checks for a blackjack in all players hands (including dealer)
    Returns Boolean
    '''
    has_blackjack = False

    for player in game_data['player_hands']:
        hand = get_hand(player, game_data)
        if is_blackjack(hand):
            if player == 'dealer':
                prompt(f'The Dealer has peeked through the hole'
                       ' and has a Blackjack!')
            else:
                prompt(f'{player} has a Blackjack!')

            has_blackjack = True
            enter_to_continue()

    return has_blackjack

def automatic_stay(hand):
    '''
    Automatic stay is triggered when players hand total reaches 21.
    Doesn't include Blackjack hand.
    '''
    return hand_total(hand) == BLACKJACK and len(hand) > CARDS_PER_HAND

def ascii_card_value_top(v, hide=False):
    if not hide:
        return f'| {str(v).ljust(2, ' ')}        |'
    return f'| ^  ^^^  ^ |'

def ascii_card_value_bottom(v, hide=False):
    if not hide:
        return f'|        {str(v).rjust(2, ' ')} |'
    return f'| ^  ^^^  ^ |'

def ascii_card_suites_display(ascii_card_suites, suite, hide=False):
    if not hide:
        return (f'{ascii_card_suites[suite]['top']}\n'
          f'{ascii_card_suites[suite]['mid_1']}\n'
          f'{ascii_card_suites[suite]['mid_2']}\n'
          f'{ascii_card_suites[suite]['bottom']}')

    return (f'{ascii_card_suites['back']['top']}\n'
          f'{ascii_card_suites['back']['mid_1']}\n'
          f'{ascii_card_suites['back']['mid_2']}\n'
          f'{ascii_card_suites['back']['bottom']}')

def display_ascii_card(card, hide=False):
    value = card['card']
    suite = card['suite']

    ascii_card_edge = '+-----------+'

    ascii_card_suites = {
        'diamonds' : {
            'top' : '|     ^     |',
            'mid_1' : '|   /   k   |',
            'mid_2' : '|   Y   /   |',
            'bottom' : '|     .     |'
        },
        'spades'   : {
            'top' : '|     .     |',
            'mid_1' : '|    /.k    |',
            'mid_2' : '|   ( . )   |',
            'bottom': '|    .^.    |'
        },
        'hearts'   : {
            'top' : '|   _   _   |',
            'mid_1' : '|  ( `V` )  |',
            'mid_2' : '|   Y. .Y   |',
            'bottom' : '|     Y     |'
        },
        'clubs'    : {
            'top' : '|     _     |',
            'mid_1' : '|    ( )    |',
            'mid_2' : '|  (_,|,_)  |',
            'bottom': '|    .^.    |'
    },
        'back' : {
            'top' : '|   ^ ^ ^   |',
            'mid_1' : '|  ^ ^^^ ^  |',
            'mid_2' : '|  ^ ^^^ ^  |',
            'bottom' : '|   ^ ^ ^   |'
        }
    }

    print(ascii_card_edge)
    if not hide:
        print(ascii_card_value_top(value))
        print(ascii_card_suites_display(ascii_card_suites, suite))
        print(ascii_card_value_bottom(value))
    else:
        print(ascii_card_value_top(value, hide=True))
        print(ascii_card_suites_display(ascii_card_suites, suite, hide=True))
        print(ascii_card_value_bottom(value, hide=True))
    print(ascii_card_edge)

def display_ascii_hand(player, game_data, dealers_turn=False):
    hand = get_hand(player, game_data)

    if not dealers_turn:
        prompt(f"{player.capitalize()}'s hand:")
    else:
        prompt(f"Dealer's hand revealed")

    for num, card in enumerate(hand):
        if player == 'dealer' and not dealers_turn:
            if num == 0:
                display_ascii_card(card)
            else:
                display_ascii_card(card, hide=True)

        else:
            display_ascii_card(card)

    if not dealers_turn and player != 'dealer':
        prompt(f'Hand total: {hand_total(hand)}')
    elif dealers_turn:
        prompt(f"Dealer's hand total: {hand_total(hand)}")
    print()

def display_hand_oneline(player, game_data):
    '''
    Display hand in oneline before dealers turn
    '''

    hand = get_hand(player, game_data)
    cards = ', '.join([card['card'] for card in hand])

    if player != 'dealer':
        print(f"({player.capitalize()}'s hand: {cards}. Total:"
              f" {hand_total(hand)})")
    else:
        print(f"(Dealers hand: {hand[0]['card']}, Unknown. Total: Unknown)")
    print()
    print('*' * len(GAME_TITLE))

# Players turn
def players_turn(hand, deck):
    prompt('Hit or Stay? (h/s)')
    answer = get_valid_input('h', 'hit', 's', 'stay')

    if answer[0].lower() == 's':
        prompt('Player chooses to stay.')
        enter_to_continue()
        return 'stay'
    else:
        new_card = deal_card(deck)
        hand.append(new_card)
        return 'hit'

# Dealer turn

def dealer_turn(hand, deck):
    dealer_hand_total = hand_total(hand)

    if dealer_hand_total >= DEALER_STAY:
        prompt(f'Dealers total is >= {DEALER_STAY}; the Dealer stays.')
        return 'stay'
    else:
        prompt('Dealer will Hit!')
        new_card = deal_card(deck)
        hand.append(new_card)
        return 'hit'
    
def turn(who, game_data, dealer=False):
    hand = get_hand(who, game_data)
    deck = game_data['deck']

    if automatic_stay(hand):
        prompt(f'{who.capitalize()} made 21, this is an automatic stay.')
        enter_to_continue()
        return
    if busted(hand):
        prompt(f'{who.capitalize()} busted!')
        prompt('Game is over.')
        return
    
    if not dealer:
        outcome = players_turn(hand, deck)
        return outcome
    else:
        outcome = dealer_turn(hand, deck)
        return outcome

def adjust_game_results(game_data, game_results):
    for player in game_data['player_hands']:
        hand = get_hand(player, game_data)
        if busted(hand):
            game_results[player] = 'bust'
        elif is_blackjack(hand):
            game_results[player] = 'blackjack'
        else:
            game_results[player] = hand_total(hand)

def game_end(game_data):
    for player in game_data['player_hands']:
        hand = get_hand(player, game_data)
        if busted(hand) or is_blackjack(hand):
            return True

    return False

# Get winner
def compare_totals(game_results):
    def get_values(key):
        '''
        Helper function for max()
        '''
        return game_results[key]

    filtered_results = {player : value for player, value in game_results.items()
                        if isinstance(value, int)}

    scores = list(filtered_results.values())
    is_draw = all([score == scores[0]for score in scores[1:]])

    if is_draw:
        return 'draw'
    return max(game_results, key=get_values)

def get_winner(game_results):
    '''
    Gets winner for 2 player games only at this stage.
    '''
    filtered_for_bust = {player : value for player, value in game_results.items()
                   if value != 'bust'}
    
    if len(filtered_for_bust) < 2:
        return list(filtered_for_bust.keys())[0]

    blackjack_winners = [winner for winner, value in filtered_for_bust.items()
                         if value == 'blackjack']

    if blackjack_winners:
        if len(blackjack_winners) < 2:
            return blackjack_winners[0]
        else:
            return 'draw'

    return compare_totals(game_results)

def display_game_results(game_results):
    def str_len(obj):
        '''
        Helper function to get length of string or integer
        '''
        if isinstance(obj, int):
            return len(str(obj))
        else:
            return len(obj)

    player_display_len = len(max(game_results.keys(), key=len))
    method_display_len = str_len(max(game_results.values(), key=str_len))
    total_display_len = player_display_len + method_display_len

    print()
    prompt('The results of this game were:')
    print('+-' + '-' * (total_display_len + 2) + '-+')
    for player in game_results:
        print(f'| {player.capitalize().ljust(player_display_len, ' ')}: '
              f'{str(game_results[player]).capitalize().ljust(method_display_len, ' ')} |')
    print('+-' + '-' * (total_display_len + 2) + '-+')
    print()

def display_winner(winner, game_results):
    display_game_results(game_results)

    if winner != 'draw':
        method = game_results[winner]
        if isinstance(method, int):
            if 'bust' not in game_results.values():
                method = 'higher total value'
            else:
                method = 'bust from other player'

        prompt(f'{winner.capitalize()} won the game via a {method}!')
    else:
        prompt('The game was a draw!')
    pass

def play_again(best_of=False):
    yes_no_options = ('y', 'yes', 'no', 'n')

    if not best_of:
        prompt('Are you ready to play the next game? (y/n)')
    else:
        prompt(f'Would you like to play another Best of {BEST_OF}? (y/n)')

    answer = get_valid_input(*yes_no_options)
    return answer.lower()[0] == 'y'

def set_up_deck():
    deck = initialize_deck()
    shuffle(deck)
    return deck

def initialize_best_of_scores(players):
    best_of_scores = {f'player{num}' : 0 for num in range(1, players + 1)}
    best_of_scores.update({'dealer' : 0})

    return best_of_scores

def display_best_of_scores(scores):
    scores_title = f'**** Best of {BEST_OF} ****'

    print()
    print(scores_title)

    for player in scores:
        line = f'{player.capitalize()} : {scores[player]}'
        print(f'* {line.center(len(scores_title) - 3, ' ')}*')

    print('*' * len(scores_title))
    print()

def update_best_of_scores(winner, scores):
    if winner != 'draw':
        scores[winner] = scores.get(winner) + 1

def end_best_of(scores):
    if sum(scores.values()) == BEST_OF:
        prompt(f'Best of {BEST_OF} game is over.')
        return True
    for player in scores:
        if scores[player] > BEST_OF // 2:
            prompt(f'Best of {BEST_OF} game terminated early. {player} has'
                   f' the majority wins out of {BEST_OF}.')
            return True
    return False

def display_best_of_winner(scores):
    def get_values(key):
        '''
        Helper function for max()
        '''
        return scores[key]

    if list(scores.values())[0] == list(scores.values())[1]:
        prompt(f'The overall game was a draw!')
    else:
        winner = max(scores, key=get_values)

        prompt(f'*** {winner.capitalize()} *** is the overall winner!')

def display_dealing_cards():
    time.sleep(1)
    prompt('Shuffling cards...')
    time.sleep(1)
    prompt('Dealing cards...')
    time.sleep(1)

def clear_and_display_scores(scores):
    clear_terminal()
    display_game_title()
    display_best_of_scores(scores)

def display_goodbye():
    prompt('Thanks for playing!')
    print('Program terminated.')

# Main
def main():
    while True:
        clear_terminal()
        display_welcome()
        if see_rules():
            display_rules()
            enter_to_continue()

        scores = initialize_best_of_scores(1)
        clear_and_display_scores(scores)
        prompt(f'This is a Best of {BEST_OF} Rounds game.')
        print()
        prompt('Are you ready to begin?')
        enter_to_continue()

        while True:
            clear_and_display_scores(scores)

            prompt('Game Start!')
            display_dealing_cards()

            # Game set up:
            clear_and_display_scores(scores)
            deck = set_up_deck()
            game_data = initialize_game_data_structure(deck)
            game_results = initialize_game_results_dict(game_data)

            deal_hands(game_data)
            prompt('Cards have been dealt.')
            display_ascii_hand('player1', game_data)
            display_ascii_hand('dealer', game_data)

            game_on = True

            if check_for_blackjack(game_data):
                clear_and_display_scores(scores)
                adjust_game_results(game_data, game_results)
                display_ascii_hand('player1', game_data)
                display_ascii_hand('dealer', game_data, dealers_turn=True)
                game_on = False
            
            enter_to_continue()

            # Player turn loop:
            while game_on:
                clear_and_display_scores(scores)
                prompt('PLAYERS TURN')
                display_ascii_hand('player1', game_data)
                display_hand_oneline('dealer', game_data)

                outcome = turn('player1', game_data)
                adjust_game_results(game_data, game_results)
                if outcome != 'hit':
                    break

            if game_end(game_data):
                enter_to_continue()

            # Dealer turn
            else:
                while True:
                    clear_and_display_scores(scores)
                    prompt('DEALERS TURN')
                    display_ascii_hand('dealer', game_data, dealers_turn=True)
                    display_hand_oneline('player1', game_data)

                    outcome = turn('dealer', game_data, dealer=True)
                    adjust_game_results(game_data, game_results)
                    enter_to_continue()
                    if outcome != 'hit':
                        break

            winner = get_winner(game_results)
            update_best_of_scores(winner, scores)
            clear_and_display_scores(scores)
            display_winner(winner, game_results)

            if end_best_of(scores):
                break

            if not play_again():
                break

        print() # Line break
        display_best_of_winner(scores)

        if not play_again(best_of=True):
            display_goodbye()
            break
main()

# TODO:
# Improve Game UX and UI using game pauses and delays etc
# Simplify main function by breaking it up into other functions
# Check all enter to continue positions, some seem unnecessary