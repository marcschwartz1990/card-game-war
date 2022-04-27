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

    def deal_cards(self, num_of_cards, players):
        """Distributes predetermined total number of cards to each player"""
        num_of_players = len(players)
        cards_per_player = int(num_of_cards/num_of_players)
        for i in range(cards_per_player):
            for player in players:
                card = self.get_random_card()
                player.cards.append(card)
        return


class Player:
    """Simulates a human or computer player"""

    def __init__(self):
        self.cards = []
