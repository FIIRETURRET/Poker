# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:49:06 2020

@author: Brandon'
"""

from Deck import StandardDeck
from Player import Player
from PokerScorer import PokerScorer

def interpreterVideoPoker():
    player = Player()
    
    # Cost per Hand
    handCost = 5
    
    
    end = False
    while not end:
        print( "You have {0} points".format(player.points) )
        print()
        
        player.points -= handCost
        
        ## Hand Loop
        # Shuffle
        deck = StandardDeck()
        deck.shuffle()
        
        # Deal Out
        for i in range(5):
            player.addCard(deck.deal())
            
        # Make them visible
        for card in player.cards:
            card.showing = True
        print(player.cards)
        
        validInput = False
        print("Which cards do you want to discard? ( ie. 1, 2, 3, 4, 5)")
        print("*Just hit return to hold all")
        while not validInput:
            inputStr = input()
            try:
                inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]
                
                for inp in inputList:
                    if inp > 6: continue
                    if inp < 1: continue
                
                for inp in inputList:
                    player.cards[inp-1] = deck.deal()
                    player.cards[inp-1].showing = True
                    
                validInput = True
                
            except:
                print("Input Error: use commas to separate the cards you want to hold")
                
            print(player.cards)
            print()
            
            # Score
            score = PokerScorer(player.cards)
            straight = score.straight()
            flush = score.flush()
            highestCount = score.highestCount()
            pairs = score.pairs()
            
            # Royal flush
            if straight and flush and straight == 14:
                print ("Royal Flush!!!")
                print ("+2000")
                player.points += 2000
            
            # Straight flush
            elif straight and flush:
                print ("Straight Flush!")
                print ("+250")
                player.points += 250
            
            # 4 of a kind
            elif score.fourKind():
                print ("Four of a Kind!")
                print ("+125")
                player.points += 125
                
            
            # Full House
            elif score.fullHouse():
                print ("Full House!")
                print ("+40")
                player.points += 40
                
            # Flush
            elif flush:
                print ("Flush!")
                print ("+25")
                player.points += 25
            
            # Straight 
            elif straight:
                print ("Straight!")
                print ("+20")
                player.points += 20
            
            # 3 of a kind
            elif highestCount == 3:
                print ("Three of a Kind!")
                print ("+15")
                player.points += 15
                
            # 2 pair
            elif len(pairs) == 2:
                print("Two Pairs!")
                print("+10")
                player.points += 10
                
            # Jacks or better
            elif pairs and pairs[0] > 10:
                print ("Jacks or Better!")
                print("+5")
                player.points += 5
                
            elif pairs and pairs[0] < 10:
                print ("Siple Pair")
                print ("+1")
                player.points += 1
                
            else:
                print("Loser")
                
            player.cards=[]
            
            print()
            print()
            print()
            
            print("Continue? (Y/N)")
            print()
            continueInput = input().strip()
            if continueInput[0] == "n" or continueInput[0] == "N":
                end = True
            
    print("Final Score {0}".format(player.points))
    print("Thank you for playing")