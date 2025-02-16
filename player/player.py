import random
from player.hand import Hand
from brain.play_selector import PlaySelector

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = Hand()

    def play_turn(self, last_played, first_move):
        playable_cards = PlaySelector(self.hand.cards).find_playable_cards(last_played, first_move)

        if not playable_cards:
            return "pass"

        weighted_choices = self._apply_weights(playable_cards)
        return random.choice(weighted_choices)

    def _apply_weights(self, playable_cards):
        """Apply weights to playable card combinations based on their size."""
        weighted_choices = []
        
        for combo in playable_cards:
            weight = len(combo) if isinstance(combo, tuple) else 1  # Single card has weight 1
            weighted_choices.extend([combo] * weight)  # Multiply probability

        return weighted_choices
