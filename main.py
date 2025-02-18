import cProfile
import pstats
import io
import os
import datetime
from game.big_two import BigTwoGame
from utils.logger import GameLogger

def play_round(game, logger):
    """Executes a single round of the game and logs it."""
    player_index = game.turn_manager.current_player
    round_num = game.turn_manager.round
    turn_count = game.turn_manager.turn_count

    print(f"Round {round_num} Turn {turn_count}")
    print(f"Player {player_index+1}'s turn")
    game.print_hands()

    # Player make a move
    player = game.players[player_index]
    move = player.play_turn(game.turn_manager.last_play, game.turn_manager.first_move)

    # Log current game state before play
    hands_state = [player.hand.sorted() for player in game.players]
    logger.log_turn(round_num, turn_count, hands_state, player_index, move)

    # Game handle the turn
    game.play_turn(player_index, move)

def main(max_rounds):
    game = BigTwoGame()
    logger = GameLogger()

    while game.turn_manager.round < max_rounds:
        play_round(game, logger)

        if game.is_game_over():
            print(f"Game over. The winner is Player {game.turn_manager.last_played_by + 1}")
            print("\n")
            logger.log_winner(game.turn_manager.last_played_by)
            break

        print()

    # Save game log at the end
    logger.save_log()

if __name__ == "__main__":
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    directory = "profiling"
    os.makedirs(directory, exist_ok=True)
    filename = os.path.join(directory, f"profile_results_{timestamp}.txt")

    # Enable profiling
    profiler = cProfile.Profile()
    profiler.enable()

    MAX_ROUNDS = 20
    main(MAX_ROUNDS)

    # Disable profiling and print stats
    profiler.disable()
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.strip_dirs().sort_stats("tottime").print_stats(20)  # Show top 20 slowest functions

    print(stream.getvalue())  # Print profiling results

    with open(filename, "w") as f:
        stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stream)
        stats.strip_dirs().sort_stats("tottime").print_stats(20)  # Show top 20 slowest functions
        f.write(stream.getvalue())  # Save results to file

    print(f"Profiling results saved to {filename}")
