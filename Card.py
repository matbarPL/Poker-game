# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:18:18 2017

@author: Mateusz
"""

class Card():
    def __init__(self, color = 0, number = 2):
        self.color = color
        self.number = number
    
    colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    numbers = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', \
               'Jack', 'Queen', 'King']
               
    def __lt__(self,other):
        if self.color > other.color:
            return False   
        if self.color < other.color:
            return True
            
        if self.number > other.number:
            return False
        if self.number < other.number:
            return True
            
        return 0
        
    def __str__(self):
        return '%s of %s' %(Card.numbers[self.number], Card.colors[self.color])

    