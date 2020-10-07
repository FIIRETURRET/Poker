# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:21:26 2020

@author: Brandon'
"""

from Card import Card

import random

class StandardDeck(list):
    def __init__(self):
        suits = {"Hearts":"♥", "Spades":"♠", "Diamonds":"◆", "Clubs":"♣"}
        values = {"Two":2,
                  "Three":3,
                  "Four":4,
                  "Five":5,
                  "Six":6,
                  "Seven":7,
                  "Eight":8,
                  "Nine":9,
                  "Ten":10,
                  "Jack":11,
                  "Queen":12,
                  "King":13,
                  "Ace":14}
        
        for name in values:
            for suit in suits:
                symbolIcon = suits[suit]
                if values[name] < 11:
                    symbol = str(values[name]) + symbolIcon
                else:
                    symbol = name[0] + symbolIcon
                self.append( Card(name, values[name], suit, symbol) )
                
    def __repr__(self):
        return "Standard deck of cards\n{0} cards remaining".format(len(self))
    
    def shuffle(self, times=1):
        random.shuffle(self)
        print("Deck Shuffled")
        
    def deal(self):
        return self.pop(0)
        