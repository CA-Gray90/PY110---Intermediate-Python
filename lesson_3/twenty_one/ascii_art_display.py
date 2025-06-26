import random

# Initializing a deck of cards:
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']
SUITES = ['diamonds', 'clubs', 'hearts', 'spades']
PLAYERS = 1
CARDS_PER_HAND = 2
COURT_CARD_VALUE = 10

def prompt(message):
    print(f'=> {message}')

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

## Get hand total
## Calculating aces:
def calc_ace(hand_total):
    '''
    Aces are worth 1 or 11 depending on context
    '''
    return 1 if hand_total >= 11 else 11

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

# Developing the function:
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

# Set up display
deck = initialize_deck()
shuffle(deck)

game_data = initialize_game_data_structure(deck)
deal_hands(game_data)
hand = get_hand('player1', game_data)

print(f'Hand dict: {hand}')
print()

display_ascii_hand('player1', game_data)
# hand = get_hand('dealer', game_data)
display_ascii_hand('dealer', game_data)
# print('Dealers Turn (hand revealed):')
display_ascii_hand('dealer', game_data, dealers_turn=True)