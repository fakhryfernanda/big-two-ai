import random
from player.hand import Hand
from brain.play_selector import PlaySelector

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = Hand()

    def play_turn(self, last_played, first_move):
        playable_cards = PlaySelector(self.hand.cards).find_playable_cards(last_played, first_move)
        return random.choice(playable_cards) if playable_cards else "pass"
