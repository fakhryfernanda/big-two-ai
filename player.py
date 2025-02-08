from collections import deque

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
