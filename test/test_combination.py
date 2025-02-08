import random
from utils.combination_finder import CombinationFinder
from game.card import Card
from constants import RANKS, SUITS

def generate_random_hand():
    """Generate a random hand of 13 unique cards."""
    deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]
    return random.sample(deck, 13)

def test_pair_finder():
    """Test finding valid pairs from a random hand."""
    hand = generate_random_hand()
    finder = CombinationFinder(hand)
    pairs = finder.find_pairs()

    print("Hand:", [str(card) for card in hand])
    print("Valid Pairs:", [(str(c1), str(c2)) for c1, c2 in pairs])

if __name__ == "__main__":
    test_pair_finder()
