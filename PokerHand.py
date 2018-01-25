# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:27:38 2017

@author: Mateusz
"""
from Card import *
from Hand import *
import sys
import operator

class PokerHand(Hand):
    def __init__(self,name):
        super().__init__(name)
        self.colors = {}
        self.numbers = {}
        
    def colors_hist(self):  
        self.colors = {}
        for card in self.cards:
            self.colors[card.color] = self.colors.get(card.color, 0) + 1
    
    def numbers_hist(self):  
        self.numbers = {}
        for card in self.cards:
            self.numbers[card.number] = self.numbers.get(card.number, 0) +1

    def inversed_numbers_hist(self):
        self.numbers_hist()
        inverse = {}
        for key in self.numbers:
            val = self.numbers[key]
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
        return inverse
            
    def has_flush(self):
        self.colors_hist()
        for val in self.colors.values():
            if val >=5:
                return True
        return False

    def has_pair(self):
        self.numbers_hist()
        for val in self.numbers.values():
            if val==2:
                return True
        return False
    
    def has_twopair(self):
        self.numbers_hist()
        i=0
        for val in self.numbers.values():
            if val==2:
                i+=1
        if i==2:
            return True
        else:
            return False

    def has_three(self):
        self.numbers_hist()
        for val in self.numbers.values():
            if val==3:
                return True
        return False
       
    def has_straight(self):
        self.numbers_hist()
        values = []
        for val in self.numbers.keys():
            values.append(val)

        i = 1
        new = []
        for i in range(3):
            new.append(values[i:i+5])
        
        for j in range(len(new)):
            for k in range(len(new[j])):
                new[j][k]=str(new[j][k]) 
                
        for el in new:
            if el in self.combinations():
                return True
        return False
        
    def combinations(self):
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', \
               '11', '12', '13']

        i = 1
        comb = []
        for i in range(9):
            comb.append(numbers[i:i+5])
        comb.append(numbers[9:14])
        l = ['1']
        comb.append((comb[9] + l))
        comb.remove(['10', '11', '12', '13'])
        return comb
        
    def has_full(self):
        if self.has_pair() and self.has_three():
             return True
        return False
        
    def has_four(self):
        self.numbers_hist()
        for val in self.numbers.values():
            if val==4:
                return True
        return False
    
    def has_poker(self):
        if self.has_straight() and self.has_flush():
            return True
        else: 
            return False
    
    def classify(self):
        t = ['0']
        classify = {'1':self.has_pair, '2':self.has_twopair, '3':self.has_three, \
                    '4':self.has_straight, '5':self.has_flush, '6':self.has_full,\
                    '7':self.has_four, '8':self.has_poker}
        
        for key,val in classify.items():
            if val() ==True:
                t.append(key + '-'+ val.__name__[4:])
        result = None
        
        t = sorted(t)
        if len(t) == 0:
            result='nothing'
        else:
            result=t[-1]
        return result
        