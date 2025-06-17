# Initializing a deck of cards:
import random
import os

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'jack', 'queen', 'king', 'ace']
SUITES = ['diamonds', 'clubs', 'hearts', 'spades']
PLAYERS = 1
CARDS_PER_HAND = 2
COURT_CARD_VALUE = 10

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
    Deals each player two cards, one at a time.
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
    return hand_total(hand) > 21

# Check for blackjack:
def is_blackjack(hand):
    '''
    Blackjack only happens when the player's first two cards equal 21.
    Automatic win.
    '''
    return hand_total(hand) == 21 and len(hand) == 2

def automatic_stay(hand):
    '''
    Automatic stay is triggered when players hand total reaches 21.
    Doesn't include Blackjack hand.
    '''
    return hand_total(hand) == 21 and len(hand) > 2

def display_hands(game_data, dealer=False):
    # Simple display of all hands for now
    # clear_terminal()
    print()
    prompt('============= DISPLAY ============')
    for player_hand in game_data['player_hands']:
        hand = get_hand(player_hand, game_data)
        if player_hand != 'dealer':
            print(f'{player_hand} : {hand}')
            print(f'Total: {hand_total(hand)}')
        elif dealer != True and player_hand == 'dealer':
            print(f'Dealers first card: {hand[0]}')
        elif dealer == True:
            print(f'Dealers hand revealed: {hand}')
            print(f'Dealers total: {hand_total(hand)}')
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

    if dealer_hand_total >= 17:
        prompt('Dealer total is >= 17; the Dealer stays.')
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

    if is_blackjack(hand):
        prompt(f'{who} got a blackjack!')
        return
    if automatic_stay(hand):
        prompt(f'{who} made 21, this is an automatic stay.')
        return
    if busted(hand):
        prompt(f'{who} busted!')
        return
    
    if dealer == False:
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

# Gets winner, does not return a tie yet.
def get_winner(game_results):
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
        # set up:
        deck = set_up_deck()
        game_data = initialize_game_data_structure(deck)
        game_results = initialize_game_results_dict(game_data)

        deal_hands(game_data)
        # display_hands(game_data)
        # player1_hand = get_hand('player1', game_data)
        # dealer_hand = get_hand('dealer', game_data)

        # Player turn:
        while True:
            display_hands(game_data)
            outcome = turn('player1', game_data)
            adjust_game_results(game_data, game_results)
            if outcome != 'hit':
                break
    
        if game_end(game_data):
            prompt('Game is over')
        else:   # Dealer Turn
            while True:
                display_hands(game_data, dealer=True)
                outcome = turn('dealer', game_data, dealer=True)
                adjust_game_results(game_data, game_results)
                if outcome != 'hit':
                    break

        print(game_results)
        get_winner(game_results)
        if not play_again():
            break

main()