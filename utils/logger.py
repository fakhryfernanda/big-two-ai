import os
import json
from game.card import Card
from config import GameConfig
from datetime import datetime

class GameLogger:
    def __init__(self):
        self.game_log = []  # Stores logs for each turn
        self.winner = None  # Stores the winner at the end
        self.initial_hands = None  # Stores the initial hands at the start

        # Ensure the log directory exists
        self.log_dir = "log"
        os.makedirs(self.log_dir, exist_ok=True)

    def log_initial_hands(self, hands_state):
        """Logs the initial hands at the start of the game."""
        self.initial_hands = {
            f"Player {i+1}": [str(card) for card in hand] for i, hand in enumerate(hands_state)
        }

    def log_turn(self, round_num, turn_count, hands_state, player, move):
        """
        Logs each turn in the specified format.
        """
        # Determine how many cards were played
        cards_played = 0 if move == "pass" else (1 if isinstance(move, Card) else len(move))
        
        turn_log = {
            "round": round_num,
            "turn": turn_count,
            "player": player + 1,  # Convert zero-based index to one-based
            "action": "pass" if move == "pass" else "play",
            "move": [] if move == "pass" else ([str(move)] if isinstance(move, Card) else [str(card) for card in move]),
            "hands_remaining": len(hands_state[player]) - cards_played  # Subtract played cards
        }

        self.game_log.append(turn_log)


    def log_winner(self, winner):
        """Logs the winner at the end of the game."""
        self.winner = f"Player {winner+1}" if winner is not None else "No winner"

    def save_log(self):
        """Saves the entire game log to a JSON file with a timestamped filename."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]  # Up to milliseconds
            
        if GameConfig.PLAYER_1_IS_USER:
            filename = os.path.join(self.log_dir, f"USER_{timestamp}.json")
        else:
            filename = os.path.join(self.log_dir, f"{timestamp}.json")

        log_data = {
            "initial_hands": self.initial_hands,
            "game_log": self.game_log,
            "winner": self.winner
        }

        with open(filename, "w") as f:
            json.dump(log_data, f, indent=4)

        print(f"Game log saved as {filename[4:]}")
