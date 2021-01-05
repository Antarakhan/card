'''
suit: hearts, diamonds, clubs
rank: 2, 3, 4 ,5, jack, queen, king
value: int value
'''
from const.const import *


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
