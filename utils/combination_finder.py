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

