from collections import deque
from game.card import Card

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.hand = deque()

    def add_card(self, card):
        """Add a card to the player's hand and keep it sorted."""
        self.hand.append(card)
        self.hand = deque(sorted(self.hand, key=lambda c: c.value()))

    def remove_cards(self, cards):
        """Remove a list of specific cards from the player's hand."""
        if isinstance(cards, Card):
            cards = (cards,)
        
        for card in cards:
            for c in self.hand:
                if c.rank == card.rank and c.suit == card.suit:
                    self.hand.remove(c)
                    return
                
        raise ValueError(f"Card {card.rank}{card.suit} is not in the player's hand!")

    def has_card(self, card):
        """Check if the player has a specific card."""
        return any(c.rank == card.rank and c.suit == card.suit for c in self.hand)

    def get_sorted_hand(self):
        """Return a sorted list of the player's hand."""
        return sorted(self.hand, key=lambda c: c.value())

    def is_hand_empty(self):
        """Check if the player has no more cards."""
        return len(self.hand) == 0
