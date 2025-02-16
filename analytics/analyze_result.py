import json
import os
from collections import defaultdict

LOGS_DIR = "log/"  # Folder where log files are stored

def analyze_game_results():
    total_games = 0
    player_wins = defaultdict(int)
    total_turns = 0
    timestamps = []

    # Loop through all JSON files in the logs directory
    for filename in os.listdir(LOGS_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(LOGS_DIR, filename)
            
            # Extract timestamp from filename (assuming format: "game_YYYYMMDD_HHMMSS.json")
            timestamp = filename.replace(".json", "")
            timestamps.append(timestamp)
            
            with open(file_path, "r") as file:
                game_data = json.load(file)

                total_games += 1
                
                # Extract winner
                winner = game_data.get("winner")
                if winner:
                    player_wins[winner] += 1

                # Count turns
                total_turns += len(game_data["game_log"])

    # Compute average turns per game
    avg_turns = total_turns / total_games if total_games > 0 else 0

    # Get timestamp range (oldest to newest)
    timestamps.sort()
    oldest = timestamps[0] if timestamps else "N/A"
    newest = timestamps[-1] if timestamps else "N/A"

    # Print the results
    print(f"Total games played: {total_games}")
    print(f"Average turns per game: {avg_turns:.2f}")
    print(f"Game timestamps: {oldest} - {newest}")
    print("Wins per player:")
    for player, wins in player_wins.items():
        print(f"  {player}: {wins} wins")

if __name__ == "__main__":
    analyze_game_results()
