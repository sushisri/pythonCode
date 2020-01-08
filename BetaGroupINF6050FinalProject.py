# !/usr/bin/env python3  
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 00:28:28 2018
@author: Beta Project Group - Cheronda B., Leigh J., Tenley S., Sushila S.
Course: INF6050 Intro to Computer Programming
School: School of Information Science, Wayne State University
Assignment: Final Group Project
"""   
#----import modules required----#
import checkExit
import requests

#----variable declaration----#

v = 'X'

## username
uName = ''

## age
uAge = 0

## gender
uGender = ''

## height
uHeight = 0

## weight
uWeight = 0

## activity level
uSedentary = 1.2
uLightActivity = 1.375
uModerateActivity = 1.55
uVeryActive = 1.725
uExtraActive = 1.9
activityLevel = 0
level = 0

## recommended calorie
rCalorie = 0

## default meal values
mainDish = 'Tofu'
sideDish1 = 'Potato'
sideDish2 = 'Rice'

#--- user defined functions ------#

# welcome message
def welcomeMessage():
    ## welcome message content
    print("\n#############################################################\n")
    print("\n\t\tWelcome to the Calorie Counter App.\n\n"+
           "This app will calculate your recommended daily calorie intake\n"+
            "and based on your last meal details will provide with the\n"+
            "amount of calories remaining.\n")
    print("#############################################################\n")
    
# user instruction
def userInstructions():
    ## user instructions content
    print("User Instructions\n")
    print("__________________\n\n")
    print("Input your demographic information to determine your daily\n"+ 
          "recommended calorie intake. After inputting your demographic\n"+
          "information, you'll be asked to input the name of an entree\n"+ 
          "and two side dishes. The calorie information of each food you\n"+
          "input will be calculated, then added together to provide the\n"+
           "total calories consumed for that meal.\n"+
          "Finally, your remaining recommended calorie intake for the\n"+ 
          "day will be displayed.\n\nType at any point type 'X' to exit.\n"+
          "\nLet's start by getting to know you a little bit.\n")
    print("__________________\n\n")

# validate number
def isNum(v):
    ## check if the user input a valid number
    print("Input is/not a valid number")
    if v.isdigit():
        if int(v)<100:
           return True
        else:
           return False
    else:
        return False
    
# thank you message does not return value or takes argument
def thankyouMessage():
    ## print thank you message
    print("\n################################################\n")
    print("\nThank you for trying the Calorie Counter App!\n")
    print("\n################################################\n")
    
# calculate recommended calories
def rCalories(uAge, uGender, uHeight, uWeight):
    ## add calorie calculation info based on the demographic data
    print("\n\nYour recommended calories\n")
    if uGender == "1":
        bmrFemale = 655.0 + (4.35 * float(uWeight)) + (4.7 * float(uHeight)) - (4.7 * float(uAge))
        rCalorie = bmrFemale * activityLevel
    elif uGender == "2":
        bmrMale = 66 + (6.23 * float(uWeight)) + (12.7 * float(uHeight)) - (6.8 * float(uHeight))
        rCalorie = bmrMale * activityLevel
    elif uGender == "3":
        bmrFemale = 655.0 + (4.35 * float(uWeight)) + (4.7 * float(uHeight)) - (4.7 * float(uAge))
        bmrMale = 66 + (6.23 * float(uWeight)) + (12.7 * float(uHeight)) - (6.8 * float(uHeight))
        rCalorie = round(((bmrMale * activityLevel) + (bmrFemale * activityLevel))/2, 2)
        
    # Truncate rcalorie so that it returns calorie intake to 2 decimal places
    print("Your recommended calorie intake should be {} calories.".format(round(rCalorie, 2)))
    return rCalorie
        
    
# print activity levels
def activityLevels():
    print("Please choose your current activity level:\n"+
          "A for sedentary\nB for lightly active\n"+ 
          "C for moderately active\nD for very active\nE for Extra active\n")

# set activity leve
def setActivity(aInput):
    if aInput == "A":
        level = 1.2
    elif aInput == "B":
        level = 1.375
    elif aInput == "C":
        level = 1.55
    elif aInput == "D":
        level = 1.725
    elif aInput == "E": 
        level = 1.9
    else:
        level = 1
        
    return level

def activityInputFunc():
    activityInput = input("Please input your activity level(A/B/C/D/E):")
    activityInput = activityInput.strip().upper()
    
# Validate input by checking if input is blank, or a character other than
# a, b, c, d, or e
# check if input is blank
    try:
        if not activityInput:
            raise ValueError
        # check if input is a character other than a, b, c, d, e
        elif (activityInput != 'A' and activityInput != 'B' and 
              activityInput != 'C' and activityInput and activityInput != 'D'
                  and activityInput != 'E' and activityInput != 'X'):
            raise ValueError
        elif activityInput == "X":
            checkExit.checkExit(v)
        else:
            return activityInput
            
    except ValueError:
        print("You must enter A, B C, D, or E. You entered: '" 
              + activityInput + "'")

        # clear out variable's value
        activityInput = None
    
        # Call activityInputFunc() again
        return activityInputFunc()

#--------------------begin main program---------------------#
welcomeMessage()
userInstructions()

#---------get valid user demographic information------------#
## get valid user activity level
activityLevels()
aInput = activityInputFunc()
activityLevel = setActivity(aInput)

## Valid gender input
while True:
    gInputs = [1,2,3]
    uGender = input("Enter 1 for Female or 2 for Male or 3 for other: ")
    try:
        i = int(uGender)
        if i in gInputs:
            break
        else:
            raise ValueError
    except:
        if uGender.strip().upper() == "X":
            checkExit.checkExit(v)

## ---get valid user weight
while True:
    uWeight = input("What is your current weight in pounds? "
                    "(Please round to the nearest whole number): ")
    try:
        val = int(uWeight)
        if val > 0:
            break
        else:
            print("Please enter a whole number.")
            raise ValueError
    except ValueError:
        if uWeight.strip().upper() == "X":
            checkExit.checkExit(v)
    
## ---get valid user age
while True:
    try:
        uAge = input("Please enter your age: ")
        if int(uAge) > 0 and int(uAge) < 120:
            break
        else:
            print("Please enter a valid age.")
            raise ValueError
    except:
        if uAge.strip().upper() == "X":
            checkExit.checkExit(v)

## --get valid user height
# validate input - can be inches or feet and inches
print("")
print("Enter your height.")
while True:
    heightFt = input("Enter feet: ")
    try:
        valFt = int(heightFt)
        if valFt > 0:
            break
        else:
            print("Please enter a whole number.")
            raise ValueError
    except ValueError:
        if heightFt.strip().upper() == "X":
            checkExit.checkExit(v)
    
while True:
    heightIn = input("Enter inches: ")
    try:
        valIn = int(heightIn)
        if valIn > 0:
            break
        else: 
            print("Please enter a whole number.")
            raise ValueError
    except ValueError:
        if heightIn.strip().upper() == "X":
            checkExit.checkExit(v)       

try:
    # convert feet and inches to only inches
    uHeight = (int(heightFt) * 12) + int(heightIn)
        
    print("You entered", heightFt + "ft", heightIn + "in")
    
    dailyCal = rCalories(uAge, uGender, uHeight, uWeight)
    
    #---------get valid user meal information------------#
    ## get valid meal type
    ## get main course (list choices collected from the api data load)
    headers = {
            'Content-Type': 'application/json',
            'x-app-id': '3e0c2836',
            'x-app-key': 'a298f0ce44cede027b12664a10b62379'
    }
    url = ' https://trackapi.nutritionix.com/v2/natural/nutrients'
    
    ## calculate and display calorie intake
    mainDish = input("Enter your entree or the main source of protein:\n "
                     "(Chicken, tofu(Default), beef or fish): ")
    
    #set default value if user does not enter a value
    if mainDish == '':
        mainDish = 'Tofu'
    json = {
         "query":mainDish,
         "timezone": "US/Eastern"
    }
    
    response = requests.post(url, headers=headers, json=json)
    mainData = response.json()
    caloriesMain = mainData['foods'][0]['nf_calories']
    
    print("Total calories for {} is: {}".format(mainDish, caloriesMain))
    
    sideDish1 = input("Enter your first side dish.(Potatoes(Default), Corn etc.: ")
    
    #set default value if user does not enter a value
    if sideDish1 == '':
        sideDish1 = 'Potatoes'
        
    json = {
         "query":sideDish1,
         "timezone": "US/Eastern"
    }
    
    response = requests.post(url, headers=headers, json=json)
    sideData1 = response.json()
    caloriesSide1 = sideData1['foods'][0]['nf_calories']
    
    print ("Total calories for {} is: {}".format(sideDish1, caloriesSide1))
    
    sideDish2 = input("Enter your second side dish for carbs.(Rice(Default), Pasta, "
                      "bread etc.): ")
    
    #set default value if user does not enter a value
    if sideDish2 == '':
        sideDish2 = 'Rice'
    
    json = {
         "query":sideDish2,
         "timezone": "US/Eastern"
    }
   
    response = requests.post(url, headers=headers, json=json)
    
    sideData2 = response.json()
    caloriesSide2 = sideData2['foods'][0]['nf_calories']
    print ("Total calories for {} is: {}".format(sideDish2, caloriesSide2))
    
    total = [float(caloriesMain), float(caloriesSide1), float(caloriesSide2)]
    totalCalories = sum(total)
    totalRemaining = round(dailyCal, 2) - totalCalories
    
    ## calculate and display how much more or less calories the user consumes
    print("\nCalories consumed for meal entered:\n", totalCalories)
    print("\nDaily recommended calories remaining:", totalRemaining)
    
    ## Thank you message
    thankyouMessage()
except:
    print("\n---Error occurred, Exiting----\n")