# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:03:11 2017

@author: Mateusz
"""
from Deck import *
class Hand():
    '''Represents a hand of playing cards'''
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        
    def take_card(self,card):
        self.cards.append(card)
        
    def pop_card(self,which):
        self.cards.pop(which)
        
    def number_of_cards(self):
        return len(self.cards)
        
    def __str__(self):
        cards = []
        for item in self.cards:
            cards.append(str(item))
        cards = '\n'.join(cards)

        return 'This is hand of ' + str(self.label) + ' player. He has ' + \
            str(len(self.cards)) + ' cards which are: \n' + str(cards)


