from deckofcards import *

deck = DeckOfCards()
p1 = Player()
p2 = Player()

print(len(deck.cards))
deck.deal_cards(26, p1, p2)
print(p1.cards)
print(p2.cards)
print(len(deck.cards))

