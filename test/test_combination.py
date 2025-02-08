import random
from utils.combination_finder import CombinationFinder
from game.card import Card
from constants import RANKS, SUITS

def generate_random_hand(size=13):
    """Generate a sorted random hand of 'size' unique cards."""
    deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    
    return sorted(deck[:size], key=lambda card: card.value())

def test_combinations(hand, combination_type, size):
    """Generic test function to find and display card combinations."""
    finder = CombinationFinder(hand)
    combinations = finder.find_combinations(size)
    print(f"{combination_type} found:", combinations)

if __name__ == "__main__":
    hand = generate_random_hand()
    print("Hand:", [str(card) for card in hand])

    test_combinations(hand, "Pairs", 2)
    test_combinations(hand, "Triples", 3)
