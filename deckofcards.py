from random import choice


class DeckOfCards:
    """Simulates a deck of playing cards"""

    card_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    card_ranks = {'2': 2, '3': 3, '4': 4,
                  '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10,
                  'J': 11, 'Q': 12, 'K': 13,
                  'A': 14,
                  }
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

    def get_card(self):
        return self.cards.pop(0)


def play_round(p1_cards, p2_cards):
    pass
    #TODO
    # Make function work for variable number of players


def evaluate_cards(p1_card, p2_card, deck, p1, p2, board):
    if deck.card_ranks[str(p1_card[0])] == deck.card_ranks[str(p2_card[0])]:
        print('war')
        reserve = []
        for i in range(2):
            reserve.append(board.pop(0))
        for i in range(3):
            p1_reserve_card = p1.cards.pop(0)
            p2_reserve_card = p2.cards.pop(0)
            reserve.append(p1_reserve_card)
            reserve.append(p2_reserve_card)
        p1_card = p1.cards.pop(0)
        p2_card = p2.cards.pop(0)
        board.append(p1_card)
        board.append(p2_card)
    elif deck.card_ranks[str(p1_card[0])] > deck.card_ranks[str(p2_card[0])]:
        print('player 1 wins!')
        p1.cards.append(p1_card)
        p1.cards.append(p2_card)
    else:
        print('player 2 wins!')
        p2.cards.append(p1_card)
        p2.cards.append(p2_card)
    #TODO
    # Make function work for variable number of players