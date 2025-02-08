from collections import defaultdict
from itertools import combinations

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
