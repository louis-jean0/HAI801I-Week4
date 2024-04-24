from treys import Deck, Evaluator, Card

def texas_holdem_round(num_players):
    deck = Deck()
    evaluator = Evaluator()
    
    player_hands = [deck.draw(2) for _ in range(num_players)]  # Cartes privées pour chaque joueur
    board_cards = deck.draw(5)  # Les cinq cartes communes (flop, turn, river)

    print("Cartes dans la rivière :", end="")
    Card.print_pretty_cards(board_cards)

    for i, hand in enumerate(player_hands):
        print(f"Joueur {i+1} : Cartes privées -", end="")
        Card.print_pretty_cards(hand)

    scores = [(evaluator.evaluate(board_cards, hand), i) for i, hand in enumerate(player_hands)]
    winner = min(scores, key=lambda x: x[0])[1]

    print(f"Le gagnant est le joueur {winner + 1} avec la main :", end="")
    Card.print_pretty_cards(player_hands[winner])
    print("Rang de la main :", evaluator.class_to_string(evaluator.get_rank_class(evaluator.evaluate(board_cards, player_hands[winner]))))

# Partie avec 4 joueurs
texas_holdem_round(4)