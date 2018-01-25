# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:29:54 2018

@author: Mateusz
"""
from Deck import *

class PokerJudge(Deck):
    def __init__(self,players):
        super().__init__(players)
        self.winners = []
        self.playersHands = []
        for i in range(self.players):
            hand = PokerHand('player nr '+ str(i+1))
            self.playersHands.append(hand)
        
    def choose_pokerwinner(self):
        classify = {'nothing':0, 'pair':1, 'twopair':2, 'three':3, 'straight':4,\
                    'flush':5, 'full':6, 'four':7, 'poker':8}
        class_dic = {}

        for item in self.playersHands:
            class_dic[item.label] = item.classify()
            
        class_dic = sorted(class_dic.items(), key=lambda x: x[1])[::-1]
        arr = class_dic[:3]
        arr = str(arr).strip('[]')
        self.winners = arr
        
    def get_pokerwinner(self):
        return self.winners
        

        
    