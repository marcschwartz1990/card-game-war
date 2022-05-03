import random

class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, None, '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of ' \
               f'{Card.suit_names[self.suit]}'

    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False

        return self.rank < other.rank


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(2, 15):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def __len__(self):
        return len(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        return self.cards.sort()

    def move_cards(self, player, num):
        """Move cards from deck to player's hand"""
        for i in range(num):
            player.add_card(self.pop_card())

    def deal_hands(self, num_of_hands, cards_per_hand):
        """Returns a list of hands"""
        hands = []
        for i in range(num_of_hands):
            hand = Hand()
            self.move_cards(hand, cards_per_hand)
            hands.append(hand)
        return hands


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


class Player(Deck):
    """Simulates a human or computer player"""

    def __init__(self):
        self.cards = []

    def get_card(self):
        return self.cards.pop(0)