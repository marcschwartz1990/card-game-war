from random import choice

class DeckOfCards:
    """Simulates a deck of playing cards"""

    card_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self.ranks = [n for n in range(2, 11)] + list('JQKA')
        self.suits = 'spades diamonds hearts clubs'.split()
        self.cards = [(rank, suit) for suit in self.suits for rank in self.ranks]

    def get_random_card(self):
        card = choice(deck.cards)
        card_idx = self.cards.index(card)
        card = self.cards.pop(card_idx)
        return card


# Provide value to each card

deck = DeckOfCards()
print(len(deck.cards))
print(deck.get_random_card())
print(len(deck.cards))