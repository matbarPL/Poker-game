# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:56:33 2017

@author: Mateusz
"""
import random
import collections
from Card import *
from PokerHand import *
 
class Deck(object):
    def __init__(self,players):
        self.cards = []
        self.players = players
        for color in range(4):
            for number in range(1,14):
                card = Card(color, number)
                self.cards.append(card)
        self.shuffle()
        self.playersHands = []
        
    def pop_card(self):
        return self.cards.pop()
        
    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort()
        
    def get_hands(self):
        return self.playersHands
    
    def move_cards(self, hand, num):
        for i in range(self.players):
            for j in range(num):
                self.playersHands[i].get_card(self.pop_card())
            
    def deal_hand(self, which, amount):
        for i in range(amount):
            self.playersHands[which].get_card(self.pop_card())
        
    def deal_hands(self, nHands, nCards):
        for i in range(nHands):
            self.move_cards(Hand(str(i)), nCards)
            self.playersHands.append(hand)
    
    def deal_to_poker(self):
        for i in range(self.players):
            hand = PokerHand('nr '+ str(i+1))
            for i in range(5):
                hand.cards.append(self.cards.pop())
            self.playersHands.append(hand)
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)



