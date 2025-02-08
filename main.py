import random
from big_two_game import BigTwoGame

def main(max_round):
    game = BigTwoGame()
    round = game.round
    
    while (round < max_round):
        player = game.current_player
        
        print(f"Round {round}")
        print(f"Player {player+1}'s turn")
        game.print_hands()

        playable_cards = game.find_playable_cards(player)
        if (len(playable_cards) > 0):
            game.play_turn(player, random.choice(playable_cards))
        else:
            game.play_turn(player, "pass")

        round = game.round

        if (game.is_game_over() == True):
            winner = game.last_played_by
            print(f"Game over. The winner is player {winner+1}")
            break

        print("\n")

if __name__ == "__main__":
    MAX_ROUND = 20
    main(MAX_ROUND)
    