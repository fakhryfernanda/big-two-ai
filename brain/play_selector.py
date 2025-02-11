import random
from utils.combination_finder import CombinationFinder
from utils.compare import compare_group

class PlaySelector:
    def __init__(self, hand):
        self.hand = hand
        self.finder = CombinationFinder(hand)
            
    def find_playable_cards(self, last_played=None):
        """Choose a valid play that beats the last played hand."""
        if not last_played:
            # No last move → Play any single card or combination
            return self.finder.find_all_combinations()

        # Determine last played type
        move_size = len(last_played)

        if move_size == 1:  # Single card play
            return [c for c in self.hand if c.value() > last_played[0].value()]

        elif move_size == 2:  # Pair
            return [pair for pair in self.finder.find_pairs() if compare_group(pair, last_played) == 1]
        
        elif move_size == 3:  # Triple
            return [triple for triple in self.finder.find_triples() if compare_group(triple, last_played) == 1]
        
        elif move_size == 4:  # Quad
            return [quad for quad in self.finder.find_quads() if compare_group(quad, last_played) == 1]
        
        else:  # Five-card play (straight, flush, full house, straight flush, royal flush)
            return self._find_stronger_five_card_play(last_played)
        
    def get_full_house_triple(self, full_house):
        """
        Given a full house (5-card hand), return the three cards that form the triple.

        Args:
            full_house (list): A list of 5 Card objects representing a full house.

        Returns:
            list: A list of 3 Card objects representing the triple.
        """
        rank_counts = {}
        
        # Count occurrences of each rank
        for card in full_house:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        # Find the rank that appears 3 times (the triple)
        triple_rank = next(rank for rank, count in rank_counts.items() if count == 3)

        # Return the three cards that match the triple rank
        return [card for card in full_house if card.rank == triple_rank]


    def _find_stronger_five_card_play(self, last_played):
        """Find a stronger five-card play based on the last move type."""
        last_play_type = self._identify_five_card_type(last_played)
        valid_moves = []

        if last_play_type == "straight":
            valid_moves = [s for s in self.finder.find_straights() if compare_group(s, last_played) == 1]
        elif last_play_type == "flush":
            valid_moves = [f for f in self.finder.find_flushes() if compare_group(f, last_played) == 1]
        elif last_play_type == "full_house":
            triple = self.get_full_house_triple(last_played)
            valid_moves = [fh for fh in self.finder.find_full_houses() if compare_group(self.get_full_house_triple(fh), triple) == 1]
        elif last_play_type == "straight_flush":
            valid_moves = [sf for sf in self.finder.find_straight_flushes() if compare_group(sf, last_played) == 1]
        elif last_play_type == "royal_flush":
            valid_moves = [rf for rf in self.finder.find_royal_flushes() if compare_group(rf, last_played) == 1]

        return valid_moves

    def _identify_five_card_type(self, five_card_hand):
        """Identify if a five-card play is a straight, flush, full house, etc."""
        suits = {card.suit for card in five_card_hand}
        ranks = sorted(card.rank for card in five_card_hand)  # Sort by numeric value

        is_flush = len(suits) == 1  # All cards have the same suit
        is_straight = ranks == list(range(int(ranks[0]), int(ranks[0]) + 5))  # Consecutive ranks

        rank_counts = {card.rank: ranks.count(card.rank) for card in five_card_hand}
        has_triple = 3 in rank_counts.values()
        has_pair = 2 in rank_counts.values()

        if is_flush and is_straight and set(ranks) == {10, 11, 12, 13, 14}:  # 10, J, Q, K, A
            return "royal_flush"
        elif is_flush and is_straight:
            return "straight_flush"
        elif has_triple and has_pair:
            return "full_house"
        elif is_flush:
            return "flush"
        elif is_straight:
            return "straight"

        raise ValueError(f"Invalid five-card combination: {five_card_hand}")

