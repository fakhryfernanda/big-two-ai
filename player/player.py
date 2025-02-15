from player.hand import Hand

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = Hand()

    def play_turn(self):
        pass