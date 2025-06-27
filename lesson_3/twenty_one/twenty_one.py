import random
import os
import pdb

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']
SUITES = ['diamonds', 'clubs', 'hearts', 'spades']

PLAYERS = 1
CARDS_PER_HAND = 2
COURT_CARD_VALUE = 10
BLACKJACK = 21
DEALER_STAY = 17
BEST_OF = 3

def prompt(message):
    print(f'=> {message}')

def clear_terminal():
    os.system('clear')

def enter_to_continue():
    prompt('Press Enter to continue...')
    input()

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
        card = card_dict['card']
        if card != 'ace':
            total += int(card) if card.isdigit() else COURT_CARD_VALUE
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
                prompt(f'The {player} has peeked through the hole'
                       ' and has a blackjack!')
            else:
                prompt(f'{player} has a Blackjack!')

            has_blackjack = True
        
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

# Players turn
def players_turn(hand, deck):
    prompt('Hit or Stay? (h/s)')
    answer = get_valid_input('h', 'hit', 's', 'stay')

    if answer[0].lower() == 's':
        prompt('Player chooses to stay.')
        return 'stay'
    else:
        prompt('Player hits!')
        new_card = deal_card(deck)
        prompt(f'New card is a {new_card['card']} of {new_card['suite']}')
        hand.append(new_card)
        return 'hit'

# Dealer turn

def dealer_turn(hand, deck):
    dealer_hand_total = hand_total(hand)

    if dealer_hand_total >= DEALER_STAY:
        prompt(f'Dealers total is >= {DEALER_STAY}; the Dealer stays.')
        return 'stay'
    else:
        print('Dealer hits!')
        new_card = deal_card(deck)
        print(f'Dealers new card: {new_card}')
        hand.append(new_card)
        return 'hit'
    
def turn(who, game_data, dealer=False):
    hand = get_hand(who, game_data)
    deck = game_data['deck']

    if automatic_stay(hand):
        prompt(f'{who} made 21, this is an automatic stay.')
        return
    if busted(hand):
        prompt(f'{who} busted!')
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

        prompt(f'{winner} won the game via a {method}!')
    else:
        prompt('The game was a draw!')
    pass

def play_again():
    prompt('Would you like to play again? (y/n)')
    answer = get_valid_input('y', 'yes', 'n', 'no')
    return answer.lower()[0] == 'y'

def set_up_deck():
    deck = initialize_deck()
    shuffle(deck)
    return deck

# Main
def main():
    while True:
        # Clear terminal
        clear_terminal()

        # set up:
        deck = set_up_deck()
        game_data = initialize_game_data_structure(deck)
        game_results = initialize_game_results_dict(game_data)

        deal_hands(game_data)
        display_ascii_hand('player1', game_data)
        display_ascii_hand('dealer', game_data)

        game_on = True

        if check_for_blackjack(game_data):
            adjust_game_results(game_data, game_results)
            display_ascii_hand('player1', game_data)
            display_ascii_hand('dealer', game_data, dealers_turn=True)
            game_on = False

        # Player turn loop:
        while game_on:
            display_ascii_hand('player1', game_data)

            outcome = turn('player1', game_data)
            adjust_game_results(game_data, game_results)
            if outcome != 'hit':
                break

        if game_end(game_data):
            prompt('Game is over.')
        # Dealer turn
        else:
            while True:
                display_ascii_hand('dealer', game_data, dealers_turn=True)
                outcome = turn('dealer', game_data, dealer=True)
                adjust_game_results(game_data, game_results)
                if outcome != 'hit':
                    break

        winner = get_winner(game_results)
        display_winner(winner, game_results)
        if not play_again():
            break

main()

# TODO:
# Improve Game UX and UI using ascii art, game pauses and delays etc