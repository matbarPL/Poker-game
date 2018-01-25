# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:08:56 2018

@author: Mateusz
"""

class Judge():
    def __init__(self):
        self.players_hands = []
        self.winners = {}
        self.nWinners = 1
        self.aWinners = []
        self.aWinnersClass = []

    def add_hand(self,hand):
        self.players_hands.append(hand)
        
    def set_nWinners(self,nWinners):
        self.nWinners = nWinners
    
    def add_hands(self,hands):
        self.players_hands = hands
    
    def remove_hand(self,hand):
        self.players_hands.remove(hand)
    
    def remove_player_by_index(self, index):
        self.players_hands.pop(index)
        
    def choose_pokerwinners(self):
        classify = {'nothing':0, 'pair':1, 'twopair':2, 'three':3, 'straight':4,\
                    'flush':5, 'full':6, 'four':7, 'poker':8}
        class_dic = {}
        
        for item in self.players_hands:
            class_dic[item.label] = item.classify()
               
        self.winners = sorted(class_dic.items(), key=lambda x: x[1])[::-1]
        
        for k,v in self.winners:
            self.aWinners.append(int(k[len(k)-1])-1)
            self.aWinnersClass.append(v)    
        
        self.aWinners = self.aWinners[:self.nWinners]
        
            
    def get_pokerwinners(self):
        return self.winners[:self.nWinners]
    
    def get_winners_hands(self):
        winnerHand = ""
        counter = 1
        for i in self.aWinners:
            winnerHand += 'Position nr ' + str(counter) +'.This player has ' +\
            self.aWinnersClass[counter-1] + '. \n' +str(self.players_hands[i]) + '\n\n'
            counter +=1
        return winnerHand
    
