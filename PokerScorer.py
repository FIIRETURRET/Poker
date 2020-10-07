# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 01:05:33 2020

@author: Brandon'
"""
from Card import Card

class PokerScorer(object):
    def __init__(self, cards):
        # Number of cards
        if not len(cards) == 5:
            return "Error: Wrong number of cards"
        self.cards = cards
    
    def flush(self):
        suits = [card.suit for card in self.cards]
        if len( set(suits) ) == 1:
            return True
        else:
            return False
    
    def straight(self):
        values = [card.value for card in self.cards]
        values.sort()
        
        if not len( set(values) ) == 5:
            return False
        
        if values[4] == 14 and values[3] == 5 and values[2] == 4 and values[1] == 3 and values[0] == 2:
            return 5
        
        else:
            if not values[0] + 1 == values[1]: return False
            if not values[1] + 1 == values[2]: return False
            if not values[2] + 1 == values[3]: return False
            if not values[3] + 1 == values[4]: return False
            
        return values[4]
    
    def highestCount(self):
        count = 0
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) > count:
                count = values.count(value)
                
        return count
    
    def pairs(self):
        pairs = []
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 2 and value not in pairs:
                pairs.append(value)
        return pairs
    
    def fourKind(self):
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 4:
                return True
            
    def fullHouse(self):
        two = False
        three = False
        
        values = [card.value for card in self.cards]
        if values.count(values) == 2:
            two = True
        if values.count(values) == 3:
            three = True
            
        if two and three:
            return True
        else: 
            return False
        
    
    
    def highCardValue(self):
        values = [card.value for card in self.cards]
        highCard = None
        for card in self.cards:
            if highCard == None:
                highCard = card
            elif highCard.value < card.value:
                highCard = card
        
        return highCard
    
    
   
        