from constants import RANKS, SUITS

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def value(self):
        return (RANKS.index(str(self.rank)), SUITS.index(self.suit))
