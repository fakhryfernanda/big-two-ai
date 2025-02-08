import random
from game.big_two import BigTwoGame
from utils.logger import GameLogger

def play_round(game, logger):
    """Executes a single round of the game and logs it."""
    player = game.turn_manager.current_player
    round_num = game.turn_manager.round
    turn_count = game.turn_manager.turn_count

    print(f"Round {round_num} Turn {turn_count}")
    print(f"Player {player+1}'s turn")
    game.print_hands()

    # Find playable cards and decide move
    playable_cards = game.find_playable_cards(player)
    move = random.choice(playable_cards) if playable_cards else "pass"

    # Log current game state before play
    hands_state = [p.get_sorted_hand() for p in game.players]
    logger.log_turn(round_num, turn_count, hands_state, player, move)

    game.play_turn(player, move)

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
    MAX_ROUNDS = 20
    main(MAX_ROUNDS)
