from treys import Card, Deck, Evaluator
import random

def monte_carlo_simulation(hole_cards, community_cards, num_simulations=1000):
    evaluator = Evaluator()
    
    hole_cards = [[Card.new(card) for card in hand] for hand in hole_cards]
    community_cards = [Card.new(card) for card in community_cards]
    
    deck = Deck()
    deck.shuffle()
    all_known_cards = [card for hand in hole_cards for card in hand] + community_cards
    
    remaining_deck = [card for card in deck.cards if card not in all_known_cards]

    results = [0] * len(hole_cards)

    for _ in range(num_simulations):
        random.shuffle(remaining_deck)
        simulated_board = community_cards + remaining_deck[:5-len(community_cards)]
        
        scores = [evaluator.evaluate(simulated_board, hand) for hand in hole_cards]
        winning_score = min(scores)
        winners = [i for i, score in enumerate(scores) if score == winning_score]

        for winner in winners:
            results[winner] += 1 / len(winners)

    probabilities = [wins / num_simulations for wins in results]
    return probabilities

player_hands = [['Ah', 'As'], ['8d', '8c']]
river = ['Ad', 'Ac', '3s']
probabilities = monte_carlo_simulation(player_hands, river, 1000)
print("Probabilités de gagner :", probabilities)
