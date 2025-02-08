class TurnManager:
    def __init__(self):
        self.current_player = 0
        self.round = 1
        self.pass_count = 0
        self.last_play = None
        self.last_played_by = None
        self.first_move = True

    def next_player(self):
        self.current_player = (self.current_player + 1) % 4

    def reset_round(self):
        self.pass_count = 0
        self.round += 1
        self.last_play = None

    def update_last_play(self, player_index, card):
        self.last_play = card
        self.last_played_by = player_index
        self.pass_count = 0
