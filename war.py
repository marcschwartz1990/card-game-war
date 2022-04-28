from deckofcards import *

deck = DeckOfCards()
p1 = Player()
p2 = Player()

players = [p1, p2]
deck.deal_cards(52, players)

# PLAY ROUND
board = []

# Get top card from each player and place on board.
p1_card = p1.get_card()
p2_card = p2.get_card()
board.append(p1_card)
board.append(p2_card)
print(board)

# Evaluate.
if deck.card_ranks[str(board[0][0])] == deck.card_ranks[str(board[1][0])]:
    print('war')
    reserve = []
    for i in range(2):
        reserve.append(board.pop(0))
    for i in range(3):
        p1_reserve_card = p1.cards.pop(0)
        p2_reserve_card = p2.cards.pop(0)
        reserve.append(p1_reserve_card)
        reserve.append(p2_reserve_card)
    p1_war_card = p1.cards.pop(0)
    p2_war_card = p2.cards.pop(0)
    board.append(p1_war_card)
    board.append(p2_war_card)
    print(reserve)
    print(board)
    #TODO
    # Evaluate board at this point. Give winning player all cards from board and reserve.
elif deck.card_ranks[str(board[0][0])] > deck.card_ranks[str(board[1][0])]:
    print('player 1 wins!')
    for card in board:
        p1.cards.append(card)
        board = []
else:
    print('player 2 wins!')
    for card in board:
        p2.cards.append(card)
        board = []

print(len(p1.cards))
print(len(p2.cards))


    #TODO
    # Turn PLAY ROUND into series of functions.
    # Create function for "war"
    # Create evaluate function