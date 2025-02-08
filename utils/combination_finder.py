from collections import defaultdict
from itertools import combinations

class CombinationFinder:
    def __init__(self, cards):
        self.cards = cards

    def find_pairs(self):
        """Find all valid pairs from the hand and sort them by rank."""
        rank_map = defaultdict(list)

        # Group cards by rank
        for card in self.cards:
            rank_map[card.rank].append(card)

        pairs = []
        # Generate all possible pairs for ranks with at least 2 cards
        for rank, cards in rank_map.items():
            if len(cards) >= 2:
                pairs.extend(combinations(cards, 2))  # Get all unique pairs

        # Sort pairs by rank (ascending) using card.value()
        pairs.sort(key=lambda pair: pair[0].value()[0])

        return pairs
