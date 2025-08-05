# Card Tools

A set of tools to create, simulate, and log card games in Python.  
This repository centers around `cardTools.py`, which provides classes and functions for deck management, hand operations, card evaluation, and common utilities for card game development.

## Features

- **Deck Management**: Create, shuffle, deal, and log cards from one or more decks.
- **Hand Operations**: Manage player hands, sort cards, calculate hand values, discard and play cards, and generate combinations for game logic like poker.
- **Card Utilities**: Convert cards into their suit, color, and value representations; sort cards; interactively load cards from user input.
- **Simulation or Real Tracking**: Can be used to simulate dealing/playing within programs or interactively to log real cards/decks/hands.

## Getting Started

### Requirements

- Python 3.x

### Usage

Import or use the classes and functions from `cardTools.py` to build your own card game logic.

#### Example: Creating and Shuffling a Deck

```python
from cardTools import Deck

deck = Deck()         # Create a standard deck
deck.shuffle()        # Shuffle the deck
print(deck.show_deck()) # Show the shuffled deck
```

#### Example: Dealing to a Single Hand

```python
from cardTools import Deck, Hand

deck = Deck()   # Initialize a deck
deck.shuffle()  # Shuffle the deck

hand = Hand(deck.deal_cards(5))     # Deal 5 cards to a hand
print(hand.show_hand())     # Show the hand
```

#### Example: Dealing Multiple Hands

```python
from cardTools import create_hands, deal_hands, Deck

deck = Deck()   # Initialize a deck
deck.shuffle()  # Shuffle the deck

hands = create_hands(4)      # Create 4 empty hands
hands, deck = deal_hands(hands, deck, num=5)  # Deal 5 cards to each hand

for i, hand in enumerate(hands):
    print(f"Player {i+1}: {hand.print_hand()}")
```

#### Example: Calculating Hand Values

```python
hand = hands[0]
print("Hand value:", hand.hand_total(ace_hi=True, face_num=False))
```

## Code Overview

### Main Classes

- **Deck**  
  Methods:
  - `shuffle()`: Shuffle the deck.
  - `deal_cards(num)`: Deal top `num` cards.
  - `log_dealt()`: Log and remove dealt cards.
  - `summary()`: Get color, suit, and value breakdown.

- **Hand**  
  Methods:
  - `show_hand()`: Display current hand.
  - `sort_hand()`: Sort cards in hand.
  - `print_hand()`: Display readable hand.
  - `add_cards(newcards)`: Add new cards.
  - `hand_total()`: Total value of the hand.
  - `discard()`: Remove a card interactively.
  - `play_cards(num)`: Play `num` cards interactively.
  - `get_combinations(num)`: All possible subgroups of cards.

### Utility Functions

- `card_value(cards, ace_hi, face_num)`: Get numeric values for cards.
- `card_suit(cards)`: Get suit names.
- `card_color(cards)`: Get card colors.
- `card_name(cards)`: Get card face names.
- `sort_cards(cards, ace_hi)`: Sort cards by value.
- `create_hands(num_players)`: Create multiple hand objects simultaneously.
- `deal_hands(hands, deck, num)`: Deal cards to multiple hands simultaneously.

### Interactive Function

- `card_loader()`: Prompts the user to enter a card (used for manual testing and interactive play).

## Customization

- **Deck size**: Pass a number to `Deck(num)` to use multiple decks.
- **Card values**: Use `ace_hi` and `face_num` booleans in value functions to support different card game rules.
  - `ace_hi` to signify if Ace is high or low
  - `face_num` to signify if face cards are all equal to 10 in value or if Jack is 11, Queen is 12, and King is 13
