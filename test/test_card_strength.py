import random
from game.card import Card
from constants import RANKS, SUITS
from utils.hand_strength_evaluator import HandStrengthEvaluator

def generate_random_hand(size=13):
    """Generate a sorted random hand of 'size' unique cards."""
    deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)

    return sorted(deck[:size], key=lambda card: card.value())

if __name__ == "__main__":
    hand = generate_random_hand()
    print("Hand:", [str(card) for card in hand])
    print()

    evaluator = HandStrengthEvaluator(hand)
    print(f"The strength of card in hand is {evaluator.evaluate_hand()}")