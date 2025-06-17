# PEDAC - Twenty One
## P
We want to create a card game in which the player plays against a computer in a 
modified version of black jack. 

### Implementation Steps:
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
    - repeat until bust or stay
4. If player busts, dealer wins
5. Dealer turn: hit or stay
    - repeat till total >= 17 or bust
6. If dealer busts, player wins
7. If neither bust, delcare highest total as winner

RULES:
- Deck is a standard deck of 52 cards
- Goal is to get as close to 21 as possible without going over, in which case you bust, and lose
- Setup: The player and dealer are both dealt two cards but the player can only see one of the dealers cards
- All card values are 1- 10, with jacks, queens and kings being 10. Ace is either 1 or 11 depending on context
    - Your program should be able to figure out whether the ace is worth 1 or 11 automatically.
- Player always goes first and can choose to hit or stay.
    - 'hit' means the player is dealth another card
    - 'stay' means they wish to stop being dealt cards and play moves to the dealer
    - If the total of the players cards goes over 21, they 'bust' and lose the game
- When it is the dealers turn, thier cards are revealed and the dealer must hit until thier total is >= 17. 
    - If they bust, they lose
- If neither bust, the totals are compared with the closest to 21 being the winner

## E

## D
Data Structure for deck of cards:
    - Deck of cards -> list of dicts (cards are nested dicts)
    - players cards -> list
    - dealers cards -> list
    
Contain all in a dict? deck of cards in a nested dict, players cards, nested list etc.
Cards taken from the deck must be removed

Avaiable cards should be a list so that we can use the shuffle method from the random module

What if we wanted to have suited cards simply for visual appeal?
    - each card would have to have 3 values, a type, a number and a color.
    - or is each card a dict itself with keys:
        - face : jack, etc
        - suit : spade
    e.g:
        deck = [{'face' : 'ace', 'suit' : 'spade'}, etc...]
    - the value is derived from the value of 'face' from the card dict.

Could this dict be used to then display an appropriate card?
random.shuffle can be used to shuffle a list of nested dicts (of cards)

#### Overall structure of Data in program:
game_data = {
    player_hand : [],
    dealer_hand : [],
    deck : [],
}

## A
High Level Implementation:
1. Initialize deck and shuffle
2. Deal two cards each to player and dealer
    - Display 2 player cards and one dealer card with other hidden
3. Check for blackjack winners?
3. Player turn: hit or stay
    - repeat until bust (total > 21) or stay
4. If player busts, dealer wins
5. Dealer turn: hit or stay
    - repeat till total >= 17 or bust
6. If dealer busts, player wins
7. If neither bust, delcare highest total as winner

## C

## Initializing a deck of cards - PEDAC:
### P
Problem:
We want to initialize a deck of cards as a list of nested dicts
each dict contains two keys: {'card' : <value is card number or court>, 'suit' : <suit>}

The 'deck' should contain all 52 cards, 13 cards for each suit
Suits: - clubs, spades, hearts, diamonds
Cards: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace

ACE value is 1, or 11

### E
Example result:
deck = [
    {'card' : 'ace', 'suit' : 'diamond'},
    {'card' : 2, 'suit' : 'diamond'},
    {'card' : 3, 'suit' : 'diamond'},
    etc...
]

A nested dict is more explicit than nested lists

### D
nested dicts in a list

### A
1. Initialize a CONSTANT to list of `SUITS` = ['diamonds', 'hearts', 'spades', 'clubs']
2. Initialize a CONSTANT to list of `CARDS` = [2, 3, 4, .. jack, queen, king, ace]
3. Initialize an empty list to `deck`
4. LOOP: for suit in suits list:
    - INNER LOOP: for card in cards list:
        - append a dict with two pairs;
            'card' as key and card as value
            'suit' as key and suit as value

### C

## Calculating Aces
Create a function that can calculate the total of a hand, including aces.

'The Ace can be worth 1 or 11 depending on circumstances. Its value is determined each time a new card is drawn from the deck. For example, if the hand contains a 2, an Ace, and a 5, then the total value of the hand is 18. In this case, the Ace is worth 11 because the sum of the hand (2 + 11 + 5) doesn't exceed 21. Now, say another card is drawn, and it happens to be an Ace. Your program must determine the value of both Aces. If the sum of the hand (2 + 11 + 5 + 11) exceeds 21, then one of the Aces must be worth 1, resulting in the hand's total value being 19. What happens if another card is drawn and it also happens to be an Ace? It can get tricky if there are multiple Aces in a hand, so your program must account for that.'

The cards being passed to the function will be either: [2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace]

The function takes a list as argument. The hand will be a list

If the total value of the cards are less than 21, the Ace should have a value of 11
If the total value of the cards are more than 21, the Ace should have a value of 1

What happens when you have more than 1 ace in the hand?
    - The first ace should have a value of 11, then 2nd 1, the 3rd 1 and so on

### E
hand_total(['ace', '2']) == 13
hand_total(['ace', '10']) == 21 # blackjack, automatic win
hand_total(['ace', '6', '4']) == 21 # automatic stay
hand_total(['ace', '4', '8', '5']) == 18 # The ace has a value of 1
hand_total(['ace', '5', '9', 'ace']) == 16 # the aces both have value of 1
hand_total(['ace', 'ace']) == 12 # One ace has a value of 11 the other: 1

### D
List of face cards to return value 10

### A
1. Get the total of all values, without aces
2. If there are aces present;
3.      If the total will be greater than 21, add 1 to the total
4.      else add 11
5. for each subsequent ace, check whether the total will go over 21 if 11 is added, else add 1

#### Helper function?
add_ace(total)

##### e 
add_ace(8) == 19
add_ace(13) == 14

Detailed Algorithm:
1. Add together all values in the list:
    - Ignore any aces
    - jack, queen, king cards have value 10

2. For each ace in the hand, check whether it will be value 11 or 1 by getting 
the total and adding 11 to it
    - if its over 21, ace should be 1
    - else its 11

3. Do step 2 while we still have aces in our hand while updating the total
4. Return the total

## Player Turn:
### P
Problem statement:
When thinking about how to code the player's turn, think about a loop that keeps
asking the player to either hit or stay. Now, think about the breaking condition for that loop.

When do we stop asking the user that question?

PCODE:
1. Ask user if they wish to hit or stay
2. If hit, deal new card:
    - If bust, player looses
    - Else goto 1
4. If stay, stop asking
    - dealers turn

Detailed Algorithm:
1. First check if they have a 'blackjack':
    - if 'blackjack', automatic win!
1. LOOP:
2. Ask user if they wish to hit or stay
3. If 'hit':
    - deal_card()
    - Calculate new total
    - IF total == 21 or busted(total):
        - break loop
    - ELSE: goto 2

4. If 'stay':
    - break loop

5. Check breaking condition:
    - IF busted(total):
        - lose game, return 'bust'?
    - ELIF 'stay':
        - dealers turn, return 'stay'?
    - ELIF total == '21':
        - 'Automatic stay'
        - dealers turn, return 'stay'?

#### Helper functions for player turn:

- Deal hands                [X]
- Deal card                 [X]
- busted                    [X]
- Check inputs              [X]
- initialize game_data dict [X]

### Deal Hands:
PEDAC
P
Problem statement:
Deal the player 2 cards and the computer 2 cards.

Technically:
    -> Player dealt one card
    -> Dealer dealt one card
    -> Player dealt 2nd card
    -> Computer dealt 2nd card

For now, this function only needs to deal cards to the player(s) and dealer. 
No need to think about displaying it.

Good to think about future implementation of more players

Cards dealt into lists for the 'hands'

E
deal_hands(game_data)

should mutate game_data dict with player_hands with two cards and dealer hand with 2 cards
deck is mutated by function

D
Recieves a game_data dict:
game_data = {
    player_hands: : {player_1 : [], dealer : []}
    deck : [],
}

Any helper functions?
deal_card() could be used within deal_hand()

Algorithm:
1. Loop through 'players' in game_data['player_hands']:
2. Deal 1 card to each player
3. Loop again; deal another card to each player

(deal card should remove and return first card from deck)

#### Helper function: Deal card
Given a deck of cards, return the first card that appears in the deck (top of the list)
Must be a destructive action (mutates the deck, removes it and returns it)
E
deal_card(deck)

D
A
- Could use .pop(0)?

#### Function that returns result of game
game_end()  
Create a function that takes the game_data and returns whether game has ended or not

Can the function be agnostic of which players turn it is?

#### Function that displays two cards of the player(s) and 1 card of the dealer
Inputs:
- game_data
- dealer_turn=False
    if True, changes what is shown

PCODE:
1. LOOP:
    For each player in game_data:
        - reveal cards (for now, print out values)
2. If dealer_turn == False:
    - do not reveal dealer second card
3. If dealer_turn == True
    - reveal second card

#### Function that displays the winner

#### Dealer Turn:
Dealer turn function:
Inputs:
- hand
- deck (mutating)

What needs to happen in the dealers turn?
1. Dealers second card is revealed > Done outside in different function.

dealer turn():
2. If blackjack;
    -> Check if player has blackjack then it is a DRAW else dealer WINS
3. LOOP:
    If dealer hand total less than 17:
        -> Dealer hits
        -> Loop until dealer hand >= 17
4. IF busted():
    Player WINS
5. IF not busted but >= 17:
    Check for winner by comparing totals > Different function outside of dealer turn

#### Determining winner:
Create a new dict called game_results that tallys results as we go?
Simpler for determining the winner at end of game.

e.g:
game_results = {
    player1 : total,
    player2 : total,
    dealer : total
}

##### Adjust Game results:
Take in the game dict, and determine game results applying them to the game
results dict.

