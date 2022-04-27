from random import choice

class DeckOfCards:
    """Simulates a deck of playing cards"""

    card_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    FULL_DECK = 52

    def __init__(self):
        self.ranks = [n for n in range(2, 11)] + list('JQKA')
        self.suits = 'spades diamonds hearts clubs'.split()
        self.cards = [(rank, suit) for suit in self.suits for rank in self.ranks]

    def get_random_card(self):
        card = choice(self.cards)
        card_idx = self.cards.index(card)
        card = self.cards.pop(card_idx)
        return card

    def deal_cards(self, num_of_cards_per_player, player_1, player_2):
        """Deals a predetermined num_of_cards_per_player from deck to 2 players"""
        for i in range(num_of_cards_per_player):
            card = self.get_random_card()
            player_1.cards.append(card)
            card = self.get_random_card()
            player_2.cards.append(card)
        return

        # for i in range(num_of_cards):





class Player:
    """Simulates a human or computer player"""

    def __init__(self):
        self.cards = []



