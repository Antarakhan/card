from random import shuffle
from const.const import *
from module.Card import Card

"""
Deck holds multiple Card objects
Deck is able to shuffle or deal cards
"""


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp
