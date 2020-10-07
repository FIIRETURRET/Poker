# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:08:24 2020

@author: Brandon'
"""

class Card( object ):
    def __init__(self, name, value, suit, symbol):
        self.value = value
        self.suit = suit
        self.name = name
        self.symbol = symbol
        self.showing = False
        
    def __repr__(self):
        if self.showing:
            return self.symbol
        else:
            return "Card"