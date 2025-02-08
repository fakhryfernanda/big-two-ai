import random
from big_two_game import BigTwoGame

def play_round(game):
    """Executes a single round of the game."""
    player = game.turn_manager.current_player
    print(f"Round {game.turn_manager.round}")
    print(f"Player {player+1}'s turn")
    game.print_hands()

    # Find playable cards and play a random one, or pass
    playable_cards = game.find_playable_cards(player)
    move = random.choice(playable_cards) if playable_cards else "pass"
    game.play_turn(player, move)

def main(max_rounds):
    game = BigTwoGame()

    while game.turn_manager.round < max_rounds:
        play_round(game)

        if game.is_game_over():
            print(f"Game over. The winner is Player {game.turn_manager.last_played_by + 1}")
            break
        print("\n")

if __name__ == "__main__":
    MAX_ROUNDS = 20
    main(MAX_ROUNDS)
