import os
import json
from game.card import Card
from config import GameConfig
from datetime import datetime

class GameLogger:
    def __init__(self):
        self.initial_hands = {}  # Stores the starting hands of each player
        self.game_log = []  # Stores logs for each round
        self.current_round = None  # Tracks the current round for simplified logging
        self.winner = None  # Stores the winner at the end

        # Ensure the log directory exists
        self.log_dir = "log"
        os.makedirs(self.log_dir, exist_ok=True)

    def log_initial_hands(self, hands_state):
        """Stores the initial hands of each player."""
        self.initial_hands = {
            f"P{i+1}": [str(card) for card in hand] for i, hand in enumerate(hands_state)
        }

    def log_turn(self, round_num, turn_count, hands_state, player, move):
        """
        Logs each turn based on the configured format.
        """
        player_id = f"P{player + 1}"
        action = "P" if move == "pass" else "play"
        move_notation = [] if move == "pass" else ([str(move)] if isinstance(move, Card) else [str(card) for card in move])
        hands_remaining = len(hands_state[player]) - (0 if move == "pass" else len(move_notation))

        if GameConfig.SIMPLIFIED_LOGGING:
            turn_entry = f"{round_num}.{turn_count} {player_id}: {'P' if move == 'pass' else '-'.join(move_notation)} H[{hands_remaining}]"

            # Group turns under a single round entry
            if not self.game_log or self.current_round != round_num:
                self.current_round = round_num
                self.game_log.append({"round": round_num, "turns": [turn_entry]})
            else:
                self.game_log[-1]["turns"].append(turn_entry)

        else:
            # Detailed logging
            turn_log = {
                "round": round_num,
                "turn": turn_count,
                "player": player_id,
                "action": action,
                "move": move_notation,
                "hands_remaining": hands_remaining
            }
            self.game_log.append(turn_log)


    def log_winner(self, winner):
        """Logs the winner at the end of the game."""
        self.winner = f"P{winner + 1}" if winner is not None else "No winner"

    def save_log(self):
        """Saves the entire game log to a JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]  # Up to milliseconds
        
        # Determine filename prefix based on config flags
        filename_prefix = "USER_" if GameConfig.PLAYER_1_IS_USER else ""
        if GameConfig.SIMPLIFIED_LOGGING:
            filename_prefix += "SIMPLIFIED_"

        filename = os.path.join(self.log_dir, f"{filename_prefix}{timestamp}.json")

        log_data = {
            "initial_hands": self.initial_hands,
            "game_log": self.game_log,
            "winner": self.winner
        }

        with open(filename, "w") as f:
            json.dump(log_data, f, indent=4)

        print(f"Game log saved as {filename[4:]}")
