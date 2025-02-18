import random
from config import GameConfig
from player.hand import Hand
from brain.play_selector import PlaySelector

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = Hand()

    def play_turn(self, last_played, first_move):
        # Chance to pass
        if random.random() < GameConfig.PASS_PROBABILITY:
            return "pass"
        
        playable_cards = PlaySelector(self.hand.cards).find_playable_cards(last_played, first_move)
        
        if not playable_cards:
            return "pass"

        weighted_choices = []
        
        for play in playable_cards:
            num_cards = len(play) if isinstance(play, tuple) else 1  # Handle single-card plays
            weight = GameConfig.WEIGHTS.get(self._get_play_type(num_cards), 1)  # Default weight = 1
            weighted_choices.extend([play] * weight)  # Add play multiple times based on weight

        return random.choice(weighted_choices)  # Choose a play randomly, considering weights
    
    def _get_play_type(self, num_cards):
        """Determine play type based on number of cards in the play."""
        if num_cards == 1:
            return "single"
        elif num_cards == 2:
            return "pair"
        elif num_cards == 3:
            return "triple"
        elif num_cards == 4:
            return "quad"
        else:
            return "five_card"
