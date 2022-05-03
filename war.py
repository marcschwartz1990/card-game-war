from Card import *

deck = Deck()
p1 = Player()
p2 = Player()

players = [p1, p2]

deck.shuffle()
deck.move_cards(p1, 26)
deck.move_cards(p2, 26)

# PLAY ROUND
board = []

# Get top card from each player and place on board.
p1_card = p1.pop_card()
p2_card = p2.pop_card()
board.append(p1_card)
board.append(p2_card)

for card in board:
    print(card)


if p1_card.rank > p2_card.rank:
    print('p1 wins')
elif p1_card.rank < p2_card.rank:
    print('p2 wins')
else:
    print('war')

#TODO:
# Create functions for p1 wins, p2 wins, war