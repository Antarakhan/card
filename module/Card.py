"""
Card class represents a single card with suit and rank
suits: hearts, diamonds, clubs
ranks: 2, 3, 4 ,5, jack, queen, king
values: int value
Calculates the value of the card
Example: Card("Clubs", "Three") then values["Three"] which is 3
"""
from const.const import *


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
