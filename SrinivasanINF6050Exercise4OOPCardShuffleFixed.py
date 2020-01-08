#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Sushila Srinivasan
Course: INF6050 Intro Computer Programming
School: School of Information Science, Wayne State University
Assignment: Excercise 4: Card Shuffling and dealing with OOP
"""

# Python program to shuffle a deck of card using the module random and draw n 
# number of cards based on user input

# import modules
from random import randint
from enum import Enum
from enum import IntEnum

deck = []
shuffleDeck = []

# creating a rank class
class Rank(IntEnum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14
    
# creating suit class
class Suit(Enum):
    Spades = 'spades'
    Clubs = 'clubs'
    Hearts = 'Hearts'
    Diamonds = 'diamonds'
    
# creating a deck of cards
class DeckOfCard:
    def __init__(self, card_rank, card_suit):
        self.card = card_rank
        self.suit = card_suit
        

#creating deck with all the suites
def create_deck():
    for suit in Suit:
        for rank in Rank:
            deck.append(DeckOfCard(Rank(rank), Suit(suit)))
    return deck
        

#drawing a random card.
def DrawCard(deck, numcards):
    for i in range(0, int(numcards)):
        randomCard = randint(0, len(deck)-1)
        random_card = deck.pop(randomCard)
        print("{} of {}".format(random_card.card, random_card.suit.name))
    return

#checking if input is a valid num between 1-5
def isInputNum(v):
    if v.isdigit():
        if int(v)>0:
            if int(v)<6:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
#creating main deck
create_deck()

#creating a secondary deck for shuffling as a list
shuffleDeck = list(deck)

#try block to catch unexpected error and print message before exiting.
#try:
valid = "No"

while valid == "No":
        # ask the user how many cards they want to deal and verify 
        # its a valid num
        numCards = input("\nHow many cards do you want to deal (1-5): ")
        if isInputNum(numCards):
                 # draw user requested number of cards and print it.
            print("\n\nYou got:")
            DrawCard(shuffleDeck, numCards)
            valid = "Yes" #valid set to yes 
                
            deal = True
            while deal == True:
                # ask the user if they want to deal again
                dealAgain = input("\nDo you want to deal again Y/N?:")
                if dealAgain.capitalize() == "Y":
                    valid = "No" # deal is set to no to loop again
                    deal = False
                    print ("\n")
                elif dealAgain.capitalize() == "N":
                    # print a thank you message and exit the program
                    print ("\n\nThank you for playing the game. Have a good day!")
                    valid = "Yes"
                    deal = False
                else:
                    print ("Please only type Y/N - any case.")                
        else:
                # print error message if invalid input is entered
                print ("Please input a valid number between 1 and 5")
#except:
#    # print error message if the program encounter unexpected error and exit
#    print ("Sorry the program encountered an error!")