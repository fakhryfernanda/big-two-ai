from collections import defaultdict
from itertools import combinations, product
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
        flushes = []
        for suit, cards in self._group_by_suit().items():
            if len(cards) >= 5:
                flushes.extend(combinations(sorted(cards, key=lambda c: c.value()), 5))
        return flushes

    def find_combinations(self, group_size):
        """Find all valid combinations (pairs, triples, quads) based on group_size."""
        combinations_list = [
            combo for cards in self._group_by_rank().values() if len(cards) >= group_size
            for combo in combinations(cards, group_size)
        ]
        return sorted(combinations_list, key=lambda combo: combo[0].value()[0])

    def find_pairs(self):
        return self.find_combinations(2)

    def find_triples(self):
        return self.find_combinations(3)

    def find_quads(self):
        return self.find_combinations(4)

    def _is_valid_straight(self, ranks):
        """Check if a given list of ranks forms a valid straight."""
        return "".join(ranks) in RANKS

    def find_straights(self):
        """Find all valid 5-card straights."""
        rank_map = self._group_by_rank()
        unique_ranks = sorted(rank_map.keys(), key=RANKS.index)
        straights = []

        for i in range(len(unique_ranks) - 4):
            consecutive_ranks = unique_ranks[i:i + 5]
            if self._is_valid_straight(consecutive_ranks):
                possible_straights = product(*[rank_map[rank] for rank in consecutive_ranks])
                straights.extend(map(tuple, possible_straights))

        return straights

    def find_full_houses(self):
        """Find all valid Full House combinations (triple first, then pair)."""
        full_houses = [
            (*triple, *pair)
            for triple in self.find_triples()
            for pair in self.find_pairs()
            if triple[0].rank != pair[0].rank  # Ensure different ranks
        ]
        return sorted(full_houses, key=lambda combo: (combo[0].value()[0], combo[3].value()[0]))

    def find_straight_flushes(self):
        """Find all valid straight flushes (5 consecutive cards of the same suit)."""
        straight_flushes = []
        for suit, cards in self._group_by_suit().items():
            if len(cards) >= 5:
                flush_straights = CombinationFinder(cards).find_straights()
                straight_flushes.extend(map(tuple, flush_straights))
        return straight_flushes

    def find_royal_flushes(self):
        """Find all Royal Flushes (A-K-Q-J-10 of the same suit)."""
        return [straight for straight in self.find_straight_flushes() if {card.rank for card in straight} == {"A", "K", "Q", "J", "0"}]
