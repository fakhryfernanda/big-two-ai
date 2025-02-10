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
    card_strings = ['3H', '4H', '5H', '5S', '6H', '6S', '7S', '8H', '9H', '9D', '9S', '9C', '0H', 'JH', 'JC', 'QH', 'KH', 'AH']
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

def test_find_full_houses(hand):
    """Test finding all valid full houses from a random hand."""
    finder = CombinationFinder(hand)
    full_houses = finder.find_full_houses()
    print("Full houses found:", full_houses)

def test_find_flush(hand):
    """Test finding all valid flush from a random hand."""
    finder = CombinationFinder(hand)
    flushes = finder.find_flushes()
    print("Flushes found:", flushes)

def test_find_straight_flush(hand):
    """Test finding all valid straight flush from a random hand."""
    finder = CombinationFinder(hand)
    straight_flushes = finder.find_straight_flushes()
    print("Straight flushes found:", straight_flushes)

def test_find_royal_flush(hand):
    """Test finding all valid royal flush from a random hand."""
    finder = CombinationFinder(hand)
    royal_flushes = finder.find_royal_flushes()
    print("Royal flushes found:", royal_flushes)

if __name__ == "__main__":
    hand = generate_random_hand()
    print("Hand:", [str(card) for card in hand])

    test_combinations(hand, "Pairs", 2)
    print()
    test_combinations(hand, "Triples", 3)
    print()
    test_combinations(hand, "Four-of-a-Kind", 4)
    print()
    test_find_straights(hand)
    print()
    test_find_full_houses(hand)
    print()
    test_find_flush(hand)
    print()
    test_find_straight_flush(hand)
    print()
    test_find_royal_flush(hand)
    print()
