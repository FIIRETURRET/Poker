# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 01:00:32 2020

@author: Brandon'
"""
import Card

class Player(object):
    def __init__(self):
        self.cards = []
        self.points = 100
        
    def cardCount(self):
        return len( self.cards )
    
    def addCard(self, card):
        self.cards.append(card)