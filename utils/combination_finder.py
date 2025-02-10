from collections import defaultdict
from itertools import combinations
from itertools import product
from constants import RANKS

class CombinationFinder:
    def __init__(self, cards):
        self.cards = cards

    def _group_by_rank(self):
        """Group cards by rank and return a dictionary."""
        rank_map = defaultdict(list)
        for card in self.cards:
            rank_map[card.rank].append(card)
        return rank_map
    
    def _group_by_suit(self):
        """Group cards by suit and return a dictionary."""
        suit_map = defaultdict(list)
        for card in self.cards:
            suit_map[card.suit].append(card)
        return suit_map
    
    def find_flushes(self):
        """Find all valid flushes (5 cards of the same suit)."""
        suit_map = self._group_by_suit()
        flushes = []

        for suit, cards in suit_map.items():
            if len(cards) >= 5:
                # Get all 5-card combinations within the same suit
                flushes.extend(combinations(sorted(cards, key=lambda c: c.value()), 5))

        return flushes

    def find_combinations(self, group_size):
        """Find all valid combinations (pairs, triples, etc.) based on group_size."""
        rank_map = self._group_by_rank()
        combinations_list = []

        for rank, cards in rank_map.items():
            if len(cards) >= group_size:
                combinations_list.extend(combinations(cards, group_size))

        # Sort combinations by rank (ascending)
        return sorted(combinations_list, key=lambda combo: combo[0].value()[0])

    def find_pairs(self):
        return self.find_combinations(2)

    def find_triples(self):
        return self.find_combinations(3)
    
    def find_quads(self):
        return self.find_combinations(4)
    
    def find_straights(self):
        """Find all valid 5-card straights from the hand."""
        rank_map = defaultdict(list)
        
        for card in self.cards:
            rank_map[card.rank].append(card)
        unique_ranks = list(rank_map.keys())
                    
        straights = []

        # Iterate over all possible 5-card straight sequences
        for i in range(len(unique_ranks) - 4):
            consecutive_ranks = unique_ranks[i:i + 5]  # Take 5 consecutive ranks
            
            # Validate: Ensure they are strictly consecutive
            expected_sequence = RANKS
            if "".join(consecutive_ranks) in expected_sequence:
                # Generate all possible straights using one card per rank
                possible_straights = product(*[rank_map[rank] for rank in consecutive_ranks])
                straights.extend([list(straight) for straight in possible_straights])

        return straights
    
    def find_full_houses(self):
        """Find all valid Full House combinations (triple first, then pair)."""
        triples = self.find_combinations(3)
        pairs = self.find_combinations(2)
        
        full_houses = []

        for triple in triples:
            for pair in pairs:
                if triple[0].rank != pair[0].rank:  # Ensure different ranks
                    full_houses.append((*triple, *pair))  # Merge into one tuple

        # Sort by the rank of the triple first, then pair
        return sorted(full_houses, key=lambda combo: (combo[0].value()[0], combo[3].value()[0]))
    
    def find_straight_flushes(self):
        """Find all valid straight flushes (5 consecutive cards of the same suit)."""
        suit_map = self._group_by_suit()
        straight_flushes = []

        for suit, cards in suit_map.items():
            if len(cards) >= 5:
                self.cards = cards
                flush_straights = self.find_straights()  # Use find_straights on same-suit cards
                straight_flushes.extend(tuple(straight) for straight in flush_straights)  # Convert to tuple

        return straight_flushes
    
    def find_royal_flushes(self):
        """Find all Royal Flushes (A-K-Q-J-10 of the same suit)."""
        straight_flushes = self.find_straight_flushes()
        royal_flushes = []

        for straight in straight_flushes:
            ranks = {card.rank for card in straight}
            if ranks == {"A", "K", "Q", "J", "0"}:  # Ensure it's exactly a Royal Flush
                royal_flushes.append(straight)

        return royal_flushes




