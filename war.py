from deckofcards import *

deck = DeckOfCards()
p1 = Player()
p2 = Player()

players = [p1, p2]

deck.deal_cards(52, players)
print(len(p1.cards))
print(len(p2.cards))

