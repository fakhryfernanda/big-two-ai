import random
from utils.combination_finder import CombinationFinder
from game.card import Card
from constants import RANKS, SUITS

def generate_random_hand(size=13):
    """Generate a sorted random hand of 'size' unique cards."""
    deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    
    return sorted(deck[:size], key=lambda card: card.value())

def generate_hand():
    card_strings = ['3H', '4D', '5C', '5H', '6H', '6S', '7H', '9H', '9S', '9D', '9C', 'JH', 'JS']
    hand = [Card(card_str[:-1], card_str[-1]) for card_str in card_strings]
    return hand

def test_combinations(hand, combination_type, size):
    """Generic test function to find and display card combinations."""
    finder = CombinationFinder(hand)
    combinations = finder.find_combinations(size)
    print(f"{combination_type} found:", combinations)

def test_find_straights(hand):
    """Test finding all valid straights from a random hand."""
    finder = CombinationFinder(hand)
    straights = finder.find_straights()
    print("Straights found:", straights)

if __name__ == "__main__":
    hand = generate_random_hand()
    print("Hand:", [str(card) for card in hand])

    test_combinations(hand, "Pairs", 2)
    test_combinations(hand, "Triples", 3)
    test_find_straights(hand)
