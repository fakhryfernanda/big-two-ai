import random
from game.card import Card
from constants import RANKS, SUITS

class HandHelper:
    @staticmethod
    def generate_random_hand(size=13):
        """Generate a sorted random hand of 'size' unique cards."""
        deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(deck)
        hand = deck[:size]
        return sorted(hand, key=lambda card: card.value())

    @staticmethod
    def generate_hand_from_list(card_list):
        """Generate a hand from a list of card representations (e.g., ['3H', '4D'])."""
        hand = [Card(card_str[0], card_str[1]) for card_str in card_list]
        return sorted(hand, key=lambda card: card.value())
    
    @staticmethod
    def print_hand(hand):
        """Print the hand in a readable format."""
        print("Hand:", [str(card) for card in hand])