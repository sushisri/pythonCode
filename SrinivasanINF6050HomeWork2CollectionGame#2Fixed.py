 # !/usr/bin/env python3  
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 21:01:26 2018

@author: Sushila Srinivasan
Course: INF6050 Intro Computer Programming
School: School of Information Science, Wayne State University
Assignment: Home Work #2 - Collection Game Part Deux
"""   
#import modules needed
import sys
import json

#initiate variables
userInfo = {'player1':{}, 'player2':{},} #emply dict
maxAttempt = 3
score = 0
attempts = 0
play = 1 #initializing player num for looping twice to get player input.
firstPlayer = ''
secondPlayer = ''

#user defined function(s)
def checkExit(v):
    if v.capitalize() == "X":
        print("\n\n")
        print("##########################################################\n")
        print("Thank you for playing. Good Bye!")
        sys.exit()
    else:
        return True

def isInputNum(v):
     if v.isdigit():
        if int(v)<100:
           return True
        else:
           return False
     else:
        return False
    
def isInputAlpha(v):
    if v.isalpha():
        return True
    else:
        return False
    
# functions find a word in a string
def result(guess, title):
    if title.startswith(guess+" "):
        return True
    if title.endswith(" "+guess):
        return True
    if title.find(" "+guess+" ") != -1:
        return True
    if title.find(guess) != -1:
        return True
    return False

# function to print welcome message and instructions
def welcome():
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    print("\t\tWelcome to the Collection Game.")
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    print("In this game we will be collecting demographic input from two\n"+
          "users and add a collection of items to each user. When you are\n"+
          "done entering your information, you will have an option to\n"+
          "play a game to guess the items in the other users collection.\n"+
          "\nAt anypoint during the game please type 'x' to quit.")
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

# guessing game Message
def gameMessage():
    print("\n\n\n\n\n\n\n\n")
    print("&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    print("Lets play the guessing game to guess what is in the\n"+ 
          "other players collections.\n")
    
    print(firstPlayer + " please turn away while,\n"+ secondPlayer +
      " guesses the title of the items in your collection")
    print("\nAt any point type 'x' if you need to quit\n")
    print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")

# thank you message
def thankMessage():
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    print("\n\t{} Thank you for playing!\n".format(guesser))
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

print ("\n------------------------Begin--------------------------\n")   
try:
    # print welcome message and instructions
    welcome()
    
    #getting player input
    while play <=2:    
        
        # updating the with player info
        if play == 1:
            player = 'player1'
        elif play == 2:
            player = 'player2'
            print("\n\n\n\n")
            welcome()
            
        # printing custom message based on the player num        
        print ("\nPlayer {} please enter your info below.\n".format(play))
        print ("------------------------------------------")
        
        # getting valid age of the player
        age = input("Please enter your age: ")
        if (checkExit(age) == True):
            validInput = False
            while validInput == False:
                if isInputNum(age):
                    age = int(age)
                    validInput = True
                else:    
                    print("Please enter a whole number less than 100 for age.")
                    age = input("Please enter your age: ")
                    checkExit(age)
        
            # if age is valid getting a valid player name            
            name = input("Please enter your first name: ")
            if (checkExit(name) == True):
                validInput = False
                while validInput == False:
                    if isInputAlpha(name):
                        validInput = True
                    else:    
                        print("Please enter letters for your name.")
                        name = input("Please enter your name: ")
                        checkExit(name)
                
                #updating the dictionary with basic user name and age
                userInfo[player].update({'name': name.capitalize(), 
                      'age': age, 'score':0 ,'attempts': 0, 
                      'collection':[]})
        
                # getting 3 title, type & year values for the users collection.
                num_items = 3 #initialling counter
                print("\nEnter {} items to fill ur collection".format(num_items))
                i=1
                while i <= num_items:
                    colTitle = input("Please enter item {} title: ".format(i))
                    if (checkExit(colTitle) == True):
                        colType = input("Please enter item {} type: ".format(i))
                        if (checkExit(colType) == True):
                            colYear = input("Please enter item {} year: ".format(i))
                            userInfo[player]['collection'].append({
                            'title': colTitle, 'type': colType, 'year': colYear})
                    i+=1
                play=play+1 #update play variable to switch players
    
    # Writing JSON data into a file
    with open('JSONData.json', 'w') as f:
        json.dump(userInfo, f)
        
    # Reading JSON data back from a file JSONData.json
    with open('JSONData.json', 'r') as f:
        data = json.load(f)
    
    #assigning player values
    firstPlayer = data['player1']['name']  
    secondPlayer = data['player2']['name']
    
    #guessing game message 
    gameMessage()
      
    # setting players and attempts
    player = firstPlayer
    guesser = secondPlayer
    guess= input("{} input a title in {}'s collection: ".format(guesser, player))
    attempts = 0
    
    #loop to play the guessing game 
    while maxAttempt>=1 :
        if checkExit(guess) == True:
            found = True
            attempts += 1
    
            if player == firstPlayer:
                collection = data['player1']['collection']
            elif player == secondPlayer:
                collection = data['player2']['collection']
        
            #iterating through the collection
            for items in collection:
                for k, v in items.items():      
                    key = str(k)
                    title = str(v)
                    title = title.lower() 
                      
                    if key.lower() == 'title':                                        
                        foundWord = result(guess, title)
    
                        #if the title is found print a message
                        if foundWord != False:
                            print("\nYay!! You got it!")
                            print("******************************************\n"+
                                  "The title is {}\n".format(title.capitalize()))
                            print("The year is {}\n".format(items['year']))
                            print("The type is {}\n".format(items['type']))
                            print("*******************"
                                  +"*****************************\n")
                            
                            thankMessage()
    
                            items['guessed']=1
                        
                            #storing values based on the players
                            if player == firstPlayer:    
                                data['player1']['score'] += 1
                                data['player1']['attempts'] = attempts
                            else:
                                data['player2']['score'] += 1
                                data['player2']['attempts'] = attempts
                                
                            #write updated data to json data file    
                            with open('JSONData.json', 'w') as f:
                                json.dump(data, f)
      
                            found = False 
                            maxAttempt = 0
                            attempts = 0
                            break 
    
            # check to updated attempts and print message for user input        
            if found == True:
                maxAttempt = maxAttempt-1 
                if maxAttempt != 0:
                    print("{} you have {} more chance(s).\n".format(guesser, maxAttempt))
                    guess= input("{} please input another title in {}'s collection: ".format(guesser, player))
     
            # check to switch players
            if maxAttempt == 0 and player == firstPlayer:
                if found == True:
                    thankMessage()
                maxAttempt = 3
                attempts = 0
                player = secondPlayer
                guesser = firstPlayer
                gameMessage()
                guess= input("{} input a title in {}'s collection: ".format(guesser, player))
except:
    print("\n\n\t\tSorry to see you leave!")
    print("\n##########################################################")

print ("\n------------------------End--------------------------\n")