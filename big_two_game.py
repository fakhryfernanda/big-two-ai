from player import Player
from deck import Deck
from turn_manager import TurnManager

class BigTwoGame:
    def __init__(self):
        self.players = [Player(i) for i in range(4)]
        self.deck = Deck()
        self.turn_manager = TurnManager()
        self.deck.deal(self.players)
        self.turn_manager.current_player = self.determine_starting_player()

    def determine_starting_player(self):
        for player in self.players:
            if player.has_card('3', 'C'):
                return player.player_id
        raise ValueError("No player has 3C! The deck might be incorrect.")

    def play_turn(self, player_index, play):
        if player_index != self.turn_manager.current_player:
            print(f"Not your turn! It's Player {self.turn_manager.current_player+1}'s turn.")
            return

        if play == "pass":
            self.handle_pass(player_index)
        else:
            self.handle_play(player_index, play)

        self.turn_manager.next_player()

    def handle_pass(self, player_index):
        self.turn_manager.pass_count += 1
        print(f"Player {player_index+1} passes.")

        if self.turn_manager.pass_count == 3:
            print("All players passed! New round starts.")
            self.turn_manager.reset_round()

    def handle_play(self, player_index, play):
        if not self.validate_move(play):
            raise ValueError(f"Invalid move by Player {player_index+1}: {play}")

        self.players[player_index].remove_card(play)
        self.turn_manager.update_last_play(player_index, play)
        print(f"Player {player_index+1} plays {play}")

        if play.rank == '3' and play.suit == 'C':
            self.turn_manager.first_move = False

    def validate_move(self, play):
        if self.turn_manager.round == 1 and self.turn_manager.first_move:
            return play.rank == '3' and play.suit == 'C'
        return self.turn_manager.last_play is None or play.value() > self.turn_manager.last_play.value()

    def is_game_over(self):
        return any(player.is_hand_empty() for player in self.players)

    def find_playable_cards(self, player_index):
        player = self.players[player_index]

        if self.turn_manager.round == 1 and self.turn_manager.first_move:
            return [card for card in player.hand if card.rank == '3' and card.suit == 'C']

        if not self.turn_manager.last_play:
            return player.hand

        return [card for card in player.hand if card.value() > self.turn_manager.last_play.value()]

    def return_hand(self, player_index):
        if player_index not in range(4):
            print("There are only 4 players")
            return None
        return self.players[player_index].get_sorted_hand()

    def print_hands(self):
        for player in self.players:
            print(f"Player {player.player_id+1}: {player.get_sorted_hand()}")
