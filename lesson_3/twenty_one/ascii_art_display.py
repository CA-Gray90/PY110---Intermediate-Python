# Initializing a deck of cards:
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'jack', 'queen', 'king', 'ace']
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

deck = initialize_deck()
game_data = initialize_game_data_structure(deck)

