from config import GameConfig
from game.card import Card
from player.player import Player
from game.deck import Deck
from game.turn_manager import TurnManager

class BigTwoGame:
    def __init__(self, predefined_hands=None):
        self.players = [Player(i) for i in range(4)]
        self.deck = Deck()
        self.turn_manager = TurnManager()

        if predefined_hands:
            self.set_predefined_hands(predefined_hands)
        else:
            self.deck.deal(self.players)  # Default random dealing

        self.turn_manager.current_player = self.determine_starting_player()

    def set_predefined_hands(self, hands):
        """Assign predefined hands to players."""
        for i in range(4):
            for card in hands[i]:
                self.players[i].hand.add_card(Card(card[0], card[1]))

    def determine_starting_player(self):
        for player in self.players:
            if player.hand.has_card(Card('3', 'C')):
                return player.player_id
        raise ValueError("No player has 3C! The deck might be incorrect.")

    def play_turn(self, player_index, play):
        if play == "pass":
            self.handle_pass(player_index)
        else:
            self.handle_play(player_index, play)

        self.turn_manager.next_player()

    def handle_pass(self, player_index):
        self.turn_manager.pass_count += 1
        
        if GameConfig.PRINT_GAME_ENABLED:
            print(f"Player {player_index+1} passes.")

        if self.turn_manager.pass_count == 3:
            if GameConfig.PRINT_GAME_ENABLED:
                print("All players passed! New round starts.")
            self.turn_manager.reset_round()

    def handle_play(self, player_index, play):
        self.players[player_index].hand.remove_cards(play)
        self.turn_manager.update_last_play(player_index, play)
        
        if GameConfig.PRINT_GAME_ENABLED:
            print(f"Player {player_index+1} plays {play}")

        if self.turn_manager.first_move:
            self.turn_manager.first_move = False

    def is_game_over(self):
        return any(player.hand.is_empty() for player in self.players)

    def return_hand(self, player_index):
        if player_index not in range(4):
            print("There are only 4 players")
            return None
        return self.players[player_index].hand.sorted()

    def print_hands(self):
        if GameConfig.PLAYER_1_IS_USER:
            if self.turn_manager.current_player == 0:
                print(f"Player 1: {self.players[0].hand.sorted()}")
            return

        for player in self.players:
            print(f"Player {player.player_id+1}: {player.hand.sorted()}")
