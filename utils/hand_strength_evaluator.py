from utils.combination_finder import CombinationFinder

class HandStrengthEvaluator:
    def __init__(self, hand):
        self.hand = hand
        self.finder = CombinationFinder(hand)
        self.scores = {
            "pair": 2,
            "triple": 5,
            "straight": 10,
            "flush": 12,
            "full_house": 15,
            "four_of_a_kind": 20,
            "straight_flush": 25,
            "royal_flush": 30,
        }
    
    def evaluate_hand(self):
        """Calculate the total strength score of the hand."""
        # Later can incorporate individual card rank into calculation
        score = 0
        
        score += len(self.finder.find_pairs()) * self.scores["pair"]
        score += len(self.finder.find_triples()) * self.scores["triple"]
        score += len(self.finder.find_straights()) * self.scores["straight"]
        score += len(self.finder.find_flushes()) * self.scores["flush"]
        score += len(self.finder.find_full_houses()) * self.scores["full_house"]
        score += len(self.finder.find_quads()) * self.scores["four_of_a_kind"]
        score += len(self.finder.find_straight_flushes()) * self.scores["straight_flush"]
        score += len(self.finder.find_royal_flushes()) * self.scores["royal_flush"]
        
        return score
