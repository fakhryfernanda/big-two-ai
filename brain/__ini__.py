import random
from utils.combination_finder import CombinationFinder

class PlaySelector:
    def __init__(self, hand):
        self.hand = hand
        self.finder = CombinationFinder(hand)
    
    def get_all_combinations(self):
        """Find all valid playable combinations from the hand."""
        combinations = []
        combinations.extend(self.finder.find_pairs())
        combinations.extend(self.finder.find_triples())
        combinations.extend(self.finder.find_quads())
        combinations.extend(self.finder.find_straights())
        combinations.extend(self.finder.find_flushes())
        combinations.extend(self.finder.find_full_houses())
        combinations.extend(self.finder.find_straight_flushes())
        combinations.extend(self.finder.find_royal_flushes())
        return combinations

    def choose_random_play(self):
        """Choose a random valid play from all possible combinations."""
        all_combinations = self.get_all_combinations()
        return random.choice(all_combinations) if all_combinations else None
