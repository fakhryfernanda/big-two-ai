import random
from card import Card
from player import Player
from contants import RANKS, SUITS

class BigTwoGame:
    def __init__(self):
        self.players = [Player(i) for i in range(4)]  # 4 player objects
        self.last_play = None  # Track the last valid play
        self.last_played_by = None  # Track the last player who played a card
        self.pass_count = 0  # Track how many players passed in a row
        self.create_deck()
        self.deal_cards()
        self.current_player = self.determine_starting_player()  # Player with 3C starts
        self.round = 0
        self.first_move = True

    def create_deck(self):
        self.deck = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.deck)

    def deal_cards(self):
        for i, card in enumerate(self.deck):
            self.players[i % 4].add_card(card)  # Add card to Player object

    def determine_starting_player(self):
        """Finds the player who has 3C and returns their index."""
        for player in self.players:
            if player.has_card('3', 'C'):
                return player.player_id
        return 0  # Fallback, should never happen

    def current_turn(self):
        """Returns the player index whose turn it is."""
        return self.current_player

    def has_valid_move(self, player_index):
        """Check if the player has any valid move."""
        player = self.players[player_index]
        return any(self.validate_move(player_index, card) for card in player.hand)

    def find_playable_cards(self, player_index):
        """Returns a list of all playable single cards for the given player."""
        player = self.players[player_index]

        if (self.round == 0 and self.first_move):
            return [card for card in player.hand if card.rank == '3' and card.suit == 'C']
        
        if not self.last_play:
            return player.hand
            
        return [card for card in player.hand if card.value() > self.last_play.value()]
    
    def play_turn(self, player_index, play):
        """Handles a player's move. 'play' is a single card or 'pass'."""
        if player_index != self.current_player:
            print(f"Not your turn! It's Player {self.current_player}'s turn.")
            return
            
        if play == "pass":
            self.pass_count += 1
            print(f"Player {player_index} passes.")

            if self.pass_count == 3:
                print("All players passed! New round starts.")
                self.last_play = None
                self.pass_count = 0
                self.round += 1
        else:
            valid_move = self.validate_move(player_index, play)
            if valid_move:
                self.players[player_index].remove_card(play)
                self.last_play = play
                self.last_played_by = player_index
                self.pass_count = 0
                print(f"Player {player_index} plays {play}")

                if (play.rank == '3' and play.suit == 'C'):
                    self.first_move = False
            else:
                print("Invalid move!")
                return
                
        self.next_player()

    def validate_move(self, player_index, play):
        """Checks if the move follows Big Two rules."""
        if self.round == 0 and self.first_move:
            return play.rank == '3' and play.suit == 'C'

        if self.last_play != None:
            return play.value() > self.last_play.value()
        
        return True
    
    def next_player(self):
        self.current_player = (self.current_player + 1) % 4
    
    def is_game_over(self):
        return any(player.is_hand_empty() for player in self.players)

    def return_hand(self, player_index):
        if player_index not in range(4):
            print("There are only 4 players")
            return None
            
        return self.players[player_index].get_sorted_hand()

    def print_hands(self):
        for player in self.players:
            print(f"Player {player.player_id}: {player.get_sorted_hand()}")
