from contants import RANKS, SUITS

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
