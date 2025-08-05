import itertools
import random


class Deck:
    def __init__(self, num=1):
        vals = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        suits = ['SB', 'DR', 'CB', 'HR']
        self.cards = [val+suit for suit in suits for val in vals]*num
        self.dealt = []

    def shuffle(self):
        random.shuffle(self.cards)

    def show_deck(self):
        return self.cards

    def deal_cards(self, num=1):
        """Deals the top cards from the deck.

        For decks that have been shuffled, used to simulate a dealer.

        :param num: Number of cards to be dealt.
        :return: The cards that were dealt.
        """
        c = self.cards[0:num]
        self.dealt.extend(c)
        self.cards = self.cards[num:]
        return c

    def log_dealt(self, ret=False, dealt_in=None):
        """Logs what cards have been dealt from the deck.

        Either takes in cards as list or prompts user to input what cards have been dealt.
        Then extends the deck's dealt list and removes the cards from the deck.

        :param ret: If True, returns the cards that have been dealt.
                Useful for simultaneously removing cards from deck and dealing to hand.
        :param dealt_in: Optional list of cards, alternative to loading in manually.
        :return: If ret=True, returns the cards that were dealt.
        """
        dealt = dealt_in if dealt_in is not None else card_loader()
        for card in dealt:
            if card in self.cards:
                self.dealt.extend([card])
                self.cards.remove(card)
            else:
                print("Card already dealt.")
                return self.log_dealt(ret=ret)
        if ret:
            return dealt

    def summary(self, ace_hi=False, face_num=False):
        """
        Returns the color makeup, suit makeup, and numeric values of the deck.
        :return: col_dict, suit_dict, vals
        """
        # Colors
        cols = card_color(self.show_deck())
        col_dict = {'Red': cols.count('Red'), 'Black': cols.count('Black')}
        # Suits
        suits = card_suit(self.show_deck())
        suit_dict = {'Spades': suits.count('Spades'), 'Diamonds': suits.count('Diamonds'),
                     'Clubs': suits.count('Clubs'), 'Hearts': suits.count('Hearts')}
        # Values
        vals = card_value(self.show_deck(), ace_hi=ace_hi, face_num=face_num)
        return col_dict, suit_dict, vals


class Hand:
    def __init__(self, cards=None):
        self.cards = cards if cards is not None else []

    def show_hand(self):
        return self.cards

    def sort_hand(self, ace_hi=False):
        """Sorts the hand's cards in place.

        :param ace_hi: If True, ace is higher than king. If False, ace is lower than 2.
        """
        self.cards = sort_cards(self.show_hand(), ace_hi=ace_hi)

    def print_hand(self):
        # COMPLETE
        return [card_name([card])[0]+' '+card_suit([card])[0] for card in self.show_hand()]

    def add_cards(self, newcards):
        """Adds cards to the hand.

        Takes in a list of cards and extends the hand's cards.

        :param newcards: List of cards to be dealt into the hand.
        """
        self.cards.extend(newcards)

    def hand_total(self, ace_hi=False, face_num=False):
        return sum(card_value(self.cards, ace_hi=ace_hi, face_num=face_num))

    def hand_values(self, ace_hi=False, face_num=False):
        return card_value(self.cards, ace_hi=ace_hi, face_num=face_num)

    def discard(self):
        """Removes a card from the hand.

        Prompts the user to input a card to be removed from the hand.
        """
        card = card_loader()
        if card in self.cards:
            self.cards.remove(card)
        else:
            print("Card not in hand.")

    def play_cards(self, num):
        """Allows the hand to play from existing cards.

        Prompts the user to input a certain number of cards to be played.
        Like discard, removes from hand, but unlike discard, returns all cards played at once.

        :param num: The number of cards to be played.
        :return: The cards played.
        """
        plays = []
        for i in range(num):
            card = card_loader()
            if card in self.cards:
                plays.append(card)
                self.cards.remove(card)
            else:
                print("Card not in hand.")
        return plays

    def get_combinations(self, num):
        """Returns all combinations of hand's cards.

        Returns all possible combinations in groups of a specified number.
        Useful for evaluating scores of sub-hands, as in poker.

        :param num: The number of cards in the sub-group. Cannot be greater than the number of cards in the hand.
        :return: A list of all hand combinations of the specified length.
        """
        return [list(com) for com in itertools.combinations(self.cards, num)]


def card_value(cards, ace_hi=False, face_num=False):
    if (ace_hi == False) and (face_num == False):
        val_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'T': 10, 'J': 10, 'Q': 10, 'K': 10}
    elif (ace_hi == True) and (face_num == False):
        val_dict = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'T': 10, 'J': 10, 'Q': 10, 'K': 10}
    elif (ace_hi == False) and (face_num == True):
        val_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    elif (ace_hi == True) and (face_num == True):
        val_dict = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    else:
        print(f"Invalid arguments.")
        return "Error"

    vals = []
    for card in cards:
        if isinstance(card, str) and len(card) == 3:
            vals.append(val_dict[card[0]])
        else:
            print(f"Invalid card type: {card}")
            vals.append(None)
    return vals


def card_suit(cards):
    suit_dict = {'H': 'Hearts', 'S': 'Spades', 'C': 'Clubs', 'D': 'Diamonds'}
    suits = []
    for card in cards:
        if isinstance(card, str) and len(card) == 3:
            suits.append(suit_dict[card[1]])
        else:
            print(f"Invalid card type: {card}")
            suits.append(None)
    return suits


def card_color(cards):
    col_dict = {'B': 'Black', 'R': 'Red'}
    colors = []
    for card in cards:
        if isinstance(card, str) and len(card) == 3:
            colors.append(col_dict[card[2]])
        else:
            print(f"Invalid card type: {card}")
            colors.append(None)
    return colors


def card_name(cards):
    name_dict = {'A': 'A', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                 '7': '7', '8': '8', '9': '9', 'T': '10', 'J': 'J', 'Q': 'Q', 'K': 'K'}
    names = []
    for card in cards:
        if isinstance(card, str) and len(card) == 3:
            names.append(name_dict[card[0]])
        else:
            print(f"Invalid card type: {card}")
            names.append(None)
    return names


def card_loader():
    card = str(input('Card: ')).upper()
    suit_color = {'S': 'B', 'C': 'B', 'H': 'R', 'D': 'R'}
    vals = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['H', 'D', 'S', 'C']

    if len(card) != 2:
        print("Entry too long.")
        return card_loader()
    else:
        if (card[0] not in vals) or (card[1] not in suits):
            print("Value not found.")
            return card_loader()
        else:
            card += suit_color[card[1]]
            print(f"{card[:2]} -> {card[0]} of {card_suit([card])[0]}")
            return [card]


def sort_cards(cards, ace_hi=False):
    if ace_hi:
        value_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    else:
        value_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    order_dict = {value: index for index, value in enumerate(value_order)}
    cards.sort(key=lambda card: order_dict[card[0]])
    return cards


def create_hands(num_players):
    hands = []
    for i in range(num_players):
        hand = Hand()
        hands.append(hand)
    return hands


def deal_hands(hands, deck, num=1):
    for hand in hands:
        hand.add_cards(deck.deal_cards(num))
    return hands, deck
