from game.card import Card
from collections import deque

class Hand:
    def __init__(self):
        self.cards = deque()

    def add_card(self, card):
        """Add a card to the playerpla's hand and keep it sorted."""
        self.cards.append(card)
        self.cards = deque(sorted(self.cards, key=lambda c: c.value()))

    def remove_cards(self, cards):
        """Remove a list of specific cards from a hand."""
        if isinstance(cards, Card):
            cards = (cards,)
        
        for card in cards:
            for c in self.cards:
                if c.rank == card.rank and c.suit == card.suit:
                    self.cards.remove(c)
                    break                
    
    def has_card(self, card):
        """Check if the player has a specific card."""
        return any(c.rank == card.rank and c.suit == card.suit for c in self.cards)

    def sorted(self):
        """Return a sorted list of cards in hand."""
        return sorted(self.cards, key=lambda c: c.value())

    def is_empty(self):
        """Check if the hand has no cards."""
        return len(self.cards) == 0