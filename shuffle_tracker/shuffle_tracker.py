# -*- coding: utf-8 -*-

cards = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
         'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
         'KD', 'QD', 'JD', '10D', '9D', '8D', '7D', '6D', '5D', '4D', '3D', '2D', 'AD',
         'KS', 'QS', 'JS', '10S', '9S', '8S', '7S', '6S', '5S', '4S', '3S', '2S', 'AS']

class Deck:
    def __init__(self):
        self.deck = cards

    def riffle_shuffle(self):
        return self.deck

    def faro(self):
        return self.deck

    def cut(self):
        return self.deck

    def find(self):
        return self.deck

    def distance(self):
        return self.deck

    def find_card_before(self):
        return self.deck

    def find_card_after(self):
        return self.deck
