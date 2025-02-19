import random
from game.card import Card
from config import GameConfig
from player.hand import Hand
from brain.play_selector import PlaySelector

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = Hand()

    def user_input_check(self):
        move_input = input("Enter your move (single card or combo, e.g., '2H' or '3D;4S' or 'pass'): ").strip()
        if move_input != '':
            move_input = move_input.upper()

        if move_input == "PASS":
            return "pass"  # Indicate that the player is skipping their turn

        # Split by semicolon to allow combos
        card_strings = move_input.split(";")
        
        if all(len(card) == 2 for card in card_strings):  # Ensure each part is exactly 2 characters
            try:
                if len(card_strings) == 1:
                    card = card_strings[0]
                    return Card(card[0], card[1])
                
                cards = tuple(Card(card[0], card[1]) for card in card_strings)  # Convert to Card objects
                return cards  # Return a list of Card objects
            except ValueError:
                print("Invalid card(s) entered. Please enter valid cards (e.g., 'AS' or '2H;3D').")
        else:
            print("Invalid input format. Enter cards as 'AS' or multiple cards separated by ';' (e.g., '2H;3D').")

    def validate_user_move(self, move, valid_moves):
        """
        Check if the given move (a single Card or a tuple of Cards) exists in the list of valid moves,
        by comparing rank and suit instead of object identity.

        :param move: A Card object (for single card) or a tuple of Card objects (for combos).
        :param valid_moves: A list containing valid moves (each move is a Card or tuple of Cards).
        :return: True if the move is in valid_moves, False otherwise.
        """
        
        # Normalize input: Always work with tuples for consistency
        move = (move,) if isinstance(move, Card) else move  

        for valid_move in valid_moves:
            # Normalize valid move to tuple as well
            valid_move = (valid_move,) if isinstance(valid_move, Card) else valid_move  
            
            # Check if all cards in move exist in valid_move (based on rank & suit)
            if len(move) == len(valid_move) and all(
                any(m.rank == v.rank and m.suit == v.suit for v in valid_move) for m in move
            ):
                return True
                
        return False

    def get_user_move(self, last_played, first_move=False):
        """Prompt the user to enter a valid move (single card or combo) and return a list of Card objects."""
        while True:
            user_input = self.user_input_check()
            if user_input == "pass":
                return "pass"
            
            playable_cards = self.get_playable_cards(last_played, first_move)
            if self.validate_user_move(user_input, playable_cards):
                return user_input
            else:
                print("Invalid move. Please enter a valid move.")

    def get_playable_cards(self, last_played, first_move=False):
        return PlaySelector(self.hand.cards).find_playable_cards(last_played, first_move)
    
    def bot_play_turn(self, last_played, first_move):
        # Chance to pass
        if random.random() < GameConfig.PASS_PROBABILITY:
            return "pass"
        
        playable_cards = self.get_playable_cards(last_played, first_move)
        
        if not playable_cards:
            return "pass"

        weighted_choices = []
        
        for play in playable_cards:
            num_cards = len(play) if isinstance(play, tuple) else 1  # Handle single-card plays
            weight = GameConfig.WEIGHTS.get(self._get_play_type(num_cards), 1)  # Default weight = 1
            weighted_choices.extend([play] * weight)  # Add play multiple times based on weight

        return random.choice(weighted_choices)  # Choose a play randomly, considering weights
    
    def _get_play_type(self, num_cards):
        """Determine play type based on number of cards in the play."""
        if num_cards == 1:
            return "single"
        elif num_cards == 2:
            return "pair"
        elif num_cards == 3:
            return "triple"
        elif num_cards == 4:
            return "quad"
        else:
            return "five_card"
