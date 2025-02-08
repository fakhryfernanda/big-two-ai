import random
from collections import deque

# Define card ranks and suits
RANKS = '34567890JQKA2'  # '0' represents 10
SUITS = 'CDHS'  # Clubs, Diamonds, Hearts, Spades (Spades highest)

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def value(self):
        return (RANKS.index(str(self.rank)), SUITS.index(self.suit))

    @classmethod
    def from_string(cls, card_str):
        """Create a Card object from a string like '3D' or '2S'."""
        if len(card_str) != 2:
            raise ValueError("Invalid card format! Use format like '3D', '2S', or '0C'.")
        rank, suit = card_str[0], card_str[1]  # Extract rank and suit
        if rank not in cls.RANKS or suit not in cls.SUITS:
            raise ValueError(f"Invalid card: {card_str}")
        return cls(rank, suit)
    
class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = deque()  # Player's hand as a deque

    def add_card(self, card):
        """Add a card to the player's hand and keep it sorted."""
        self.hand.append(card)
        self.hand = deque(sorted(self.hand, key=lambda c: c.value()))

    def remove_card(self, card):
        """Remove a specific card from the player's hand."""
        for c in self.hand:
            if c.rank == card.rank and c.suit == card.suit:
                self.hand.remove(c)
                return True  # Successfully removed
        print(f"{card} is not in player {self.player_id}'s hand!")
        return False

    def has_card(self, rank, suit):
        """Check if the player has a specific card."""
        return any(c.rank == rank and c.suit == suit for c in self.hand)

    def get_sorted_hand(self):
        """Return a sorted list of the player's hand."""
        return sorted(self.hand, key=lambda c: c.value())

    def is_hand_empty(self):
        """Check if the player has no more cards."""
        return len(self.hand) == 0

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


if __name__ == "__main__":
    game = BigTwoGame()
    round = game.round
    
    while (round < 20):
        player = game.current_player
        
        print(f"Round {round}")
        print(f"Player {player}'s turn")
        game.print_hands()

        playable_cards = game.find_playable_cards(player)
        if (len(playable_cards) > 0):
            game.play_turn(player, random.choice(playable_cards))
        else:
            game.play_turn(player, "pass")

        round = game.round

        if (game.is_game_over() == True):
            winner = game.last_played_by
            print(f"Game over. The winner is player {winner}")
            break

        print("\n")