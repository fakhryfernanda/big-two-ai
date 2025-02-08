import os
import json
from datetime import datetime

class GameLogger:
    def __init__(self):
        self.game_log = []  # Stores logs for each turn
        self.winner = None  # Stores the winner at the end

        # Ensure the log directory exists
        self.log_dir = "log"
        os.makedirs(self.log_dir, exist_ok=True)

    def log_turn(self, round_num, turn_count, hands_state, player, move):
        """
        Logs each turn in a structured JSON-serializable format.
        """
        serialized_hands = {f"Player {i+1}": [str(card) for card in hand] for i, hand in enumerate(hands_state)}

        move_entry = {
            "player": player + 1,  # Convert zero-based index to one-based
            "action": str(move) if move != "pass" else "pass"
        }

        turn_log = {
            "round": round_num,
            "turn": turn_count,
            "hands": serialized_hands,
            "move": move_entry
        }

        self.game_log.append(turn_log)

    def log_winner(self, winner):
        """Logs the winner at the end of the game."""
        self.winner = f"Player {winner+1}" if winner is not None else "No winner"

    def save_log(self):
        """Saves the entire game log to a JSON file with a timestamped filename."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]  # Up to milliseconds
        filename = os.path.join(self.log_dir, f"{timestamp}.json")

        log_data = {
            "game_log": self.game_log,
            "winner": self.winner
        }

        with open(filename, "w") as f:
            json.dump(log_data, f, indent=4)

        print(f"Game log saved as {filename[4:]}")
