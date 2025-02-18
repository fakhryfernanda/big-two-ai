import os
import datetime
from config import GameConfig
from profiling import GameProfiler
from game.big_two import BigTwoGame
from utils.logger import GameLogger

def play_round(game, logger):
    """Executes a single round of the game and logs it."""
    player_index = game.turn_manager.current_player
    game_state = {
        'round': game.turn_manager.round,
        'turn': game.turn_manager.turn_count,
        'player': player_index
    }

    # Print game state if PRINT_GAME_ENABLED is set to True
    if GameConfig.PRINT_GAME_ENABLED:
        print()
        print(f"Round {game_state['round']} Turn {game_state['turn']}")
        print(f"Player {player_index + 1}'s turn")
        game.print_hands()

    # Player makes a move
    player = game.players[player_index]
    move = player.play_turn(game.turn_manager.last_play, game.turn_manager.first_move)

    # Log game state if logging is enabled
    if logger:
        hands_state = [player.hand.sorted() for player in game.players]
        logger.log_turn(game_state['round'], game_state['turn'], 
                       hands_state, player_index, move)

    game.play_turn(player_index, move)

def run_game(max_rounds, logger=None):
    """Runs the main game loop."""
    game = BigTwoGame()

    while game.turn_manager.round < max_rounds:
        play_round(game, logger)

        if game.is_game_over():
            winner = game.turn_manager.last_played_by
            print(f"Game over. The winner is Player {winner + 1}")
            if logger:
                logger.log_winner(winner)
            break

    if logger:
        logger.save_log()

def main():
    if GameConfig.PROFILING_ENABLED:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs(GameConfig.PROFILE_DIR, exist_ok=True)
        profile_file = os.path.join(GameConfig.PROFILE_DIR, 
                                   f"profile_results_{timestamp}.txt")
        
        # Initialize profiler
        profiler = GameProfiler(GameConfig.PROFILE_DIR, GameConfig.TOP_STATS_COUNT)
        logger = GameLogger() if GameConfig.LOGGING_ENABLED else None
        
        # Run with profiling
        profiler.start()
        run_game(GameConfig.MAX_ROUNDS, logger)
        profiler.stop()
        
        # Save and display results
        results = profiler.save_results(profile_file)
        print(results)
        print(f"Profiling results saved to {profile_file}")
    else:
        # Run without profiling
        logger = GameLogger() if GameConfig.LOGGING_ENABLED else None
        run_game(GameConfig.MAX_ROUNDS, logger)


if __name__ == "__main__":
    main()
