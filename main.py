 # -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:20:12 2018

@author: Mateusz
"""
from Card import *
from Deck import *
from Judge import *
from PokerHand import *

if __name__ =="__main__":    
    deck = Deck(5)
    deck.deal_to_poker()
    judge = Judge()
    judge.set_nWinners(3)
    judge.add_hands(deck.get_hands())
    judge.choose_pokerwinners()
    print (judge.get_winners_hands())