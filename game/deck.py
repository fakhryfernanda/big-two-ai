import random
from game.card import Card
from constants import RANKS, SUITS

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

    def deal(self, players):
        """Deals cards evenly to players."""
        for i, card in enumerate(self.cards):
            players[i % 4].hand.add_card(card)
