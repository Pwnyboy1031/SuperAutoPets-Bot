
from tabnanny import check
from turtle import update
from xml.dom.minidom import Element
from xml.etree.ElementInclude import include
import pyautogui
import time
import random
import cv2
import numpy


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.5

#shop/team vertical coordinates
teamy = 338
shopy = 605 
#Y coordinates to check if pets are empty
#horizontal coordinates for play
pos1x = 476
pos2x = 620 
pos3x = 753 
pos4x = 890
pos5x = 1026
#items
pos6x = 1160
pos7x = 1293

#Endturn Coordinates
END_TURN_X = 1623
END_TURN_Y = 943

Gold = 10
Turn = 1

#Team Array
Team = [pos1x,pos2x,pos3x,pos4x,pos5x]

Squad = []
currentShop = []

#TierList
TierList = ["fish","ant","beaver","mosquito","cricket","otter","horse","pig","duck"]

#Pet Dictionary
petDict = {
    "pet": "ant.png",
    "name": "ant",
    "attack": 2,
    "health": 1,
    "ability": "faint"
}

def update():
    global currentShop
    currentShop = []
    findGold()
    identifyTeam()
    identifyShop()

#Start Countdown
def start_countdown():
    print("Starting", end="", flush= True)
    for i in range(0, 5):
        print(".", end="", flush= True)
        time.sleep(1)
    print("Go")

def start_game():
    pyautogui.moveTo(971,510)
    pyautogui.click()

def buy_pet(position,pet):
    #Choose pet
    findPetShop(pet,"shop")
    pyautogui.click()
    #Buy pet at position
    pyautogui.click(position+50,teamy)
    findGold()

def end_turn():
    global Turn
    #End the turn and battle
    pyautogui.moveTo(1623, 943)
    pyautogui.click()
    if (pyautogui.locateOnScreen("excessgold.png", confidence = .9)) != None:
        pyautogui.click("confirmbutton.PNG")

    Turn += 1
    #Speed up game
    time.sleep(3)
    pyautogui.click(50,50)
    time.sleep(15)
    checkWin()

def upgradeTeamPet():
    for pet in currentShop:
        if pet == Squad[0]:
            buy_pet(pos1x,pet)
            break
        elif pet == Squad[1]:
            buy_pet(pos2x,pet)
            break
        elif pet == Squad[2]:
            buy_pet(pos3x,pet)
            break
        elif pet == Squad[3]:
            buy_pet(pos4x,pet)
            break
        elif pet == Squad[4]:
            buy_pet(pos5x,pet)
            break




def roll():
        pyautogui.moveTo(178, 946)
        pyautogui.click()
    
#Finds current gold count
def findGold():
    global Gold
    if (pyautogui.locateCenterOnScreen("10gold.png") != None):
        Gold = 10
    elif (pyautogui.locateCenterOnScreen("9gold.png") != None):
        Gold = 9
    elif (pyautogui.locateCenterOnScreen("8gold.png") != None):
        Gold = 8
    elif (pyautogui.locateCenterOnScreen("7gold.png") != None):
        Gold = 7
    elif (pyautogui.locateCenterOnScreen("6gold.png") != None):
        Gold = 6
    elif (pyautogui.locateCenterOnScreen("5gold.png") != None):
        Gold = 5
    elif (pyautogui.locateCenterOnScreen("4gold.png") != None):
        Gold = 4
    elif (pyautogui.locateCenterOnScreen("3gold.png") != None):
        Gold = 3
    elif (pyautogui.locateCenterOnScreen("2gold.png") != None):
        Gold = 2
    elif (pyautogui.locateCenterOnScreen("1gold.png") != None):
        Gold = 1
    else:
        Gold = 0
    print("The current gold count is", Gold)

# Checks if the slot selected is empty
def check_Slot_Empty(x,y):
    if pyautogui.locateOnScreen("empty.png", region=(x,y,200,300,)) != None or pyautogui.pixelMatchesColor(x+75, y+100, (186, 178, 145))  == True:
        return True
    else: 
        print("Position is filled!") 
        return False

def checkWin():
    if (pyautogui.locateOnScreen("victory.png", confidence= .9) != None):
        print("We won! :)")
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(pos1x,shopy)
        pyautogui.click()
    elif (pyautogui.locateOnScreen("defeat.png", confidence= .9) != None): 
        print("We lost ! :(")
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(pos1x,shopy)
        pyautogui.click()
    elif (pyautogui.locateOnScreen("draw.png", confidence= .7) != None):
        print("We tied. :|")
    elif(pyautogui.locateOnScreen("gameover.png", confidence= .7) != None):
        print("Game over! X(")
    else:print("WE WON! XD")
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(pos1x,shopy)
    pyautogui.click()

def buyItem():
    global Gold
    while (Gold >= 3):
        if check_Slot_Empty(pos7x,shopy) == False:
            pyautogui.click(pos7x+10,shopy)
            selection = random.randint(1,5)
            if selection == 1:
                pyautogui.click(pos1x,teamy)
                findGold()
            elif selection == 2:
                pyautogui.click(pos2x,teamy)
                findGold()
            elif selection == 3:
                pyautogui.click(pos3x,teamy)
                findGold()
            elif selection == 4:
                pyautogui.click(pos4x,teamy)
                findGold()
            else:
                pyautogui.click(pos5x,teamy)
                findGold()
        else: 
            roll()
            findGold()


#Looks for a specific pet in the shop, or buy first shop position
def findPetShop(pet,shopOrTeam):
    if shopOrTeam == "shop" and pet != "any":
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(pet + ".png", confidence=.40, region=(450,600, 1000,200)))
    elif pet == "any":
        pyautogui.moveTo(pos1x+20,shopy+20)
    else: pyautogui.moveTo(pyautogui.locateCenterOnScreen(pet + ".png", confidence=.40, region=(450,320, 1000,200)))

def identifyPet(x,y):
    TierList
    for pet in TierList:
        if pyautogui.locateCenterOnScreen(pet + ".png", confidence=.40, region=(x,y, 200,250)) != None:
            return(pet)

def identifyShop():
    for pos in Team:
        currentShop.append(identifyPet(pos,shopy))

def identifyTeam():
    global Squad
    Squad = []
    for x in Team:
        Squad.append(identifyPet(x,teamy))

def chooseNextAction():
    buyAnt = 0
    buyFish = 0
    buyBeaver = 0
    buyDuck = 0
    buyHorse = 0
    buyMosquito = 0
    buyPig = 0
    buyOtter = 0
    buyCricket = 0
    buyItems = 0
    rollShop = 0
    endTurn = 0
    upgradePet = 0
    buyRandomPet = 0
    possibleDecisions = []

    
    update()
    print(Squad)
    for pet in currentShop:
        if pet == "ant":
            buyAnt = buyAnt + 50
        elif pet == "fish":
            buyFish = buyFish + 51
        elif pet == "beaver":
            buyBeaver = buyBeaver + 35
        elif pet == "duck":
            buyDuck = buyDuck + 5
        elif pet == "horse":
            buyHorse = buyHorse + 10
        elif pet == "mosquito":
            buyMosquito = buyMosquito + 40
        elif pet == "pig":
            buyPig = buyPig + 7
        elif pet == "otter":
            buyOtter = buyOtter + 25
        elif pet == "cricket": 
            buyCricket = buyCricket + 30

    #Check if upgrade is viable        
    if None not in Squad:
        for pet in currentShop:
            if pet == Squad[0]:
                upgradePet += 60
            elif pet == Squad[1]:
                upgradePet += 60
            elif pet == Squad[2]:
                upgradePet += 60
            elif pet == Squad[3]:
                upgradePet += 60
            elif pet == Squad[4]:
                upgradePet += 60
    
    if Gold > 3:
        buyRandomPet += 20


    if Gold > 3 and None not in Squad:
        buyItems += 90
    
    if Gold < 3:
        endTurn += 100

    possibleDecisions = [buyAnt, buyFish, buyBeaver, buyDuck, buyHorse, buyMosquito, buyPig, buyOtter, buyCricket, buyItems, rollShop, endTurn, upgradePet,buyRandomPet]
    print(possibleDecisions)

    if max(possibleDecisions) == buyAnt:
        buy_pet(pos1x,"ant")
    elif max(possibleDecisions) == buyFish:
        buy_pet(pos1x,"fish")
    elif max(possibleDecisions) == buyBeaver:
        buy_pet(pos1x,"beaver")
    elif max(possibleDecisions) == buyDuck:
        buy_pet(pos1x,"duck")
    elif max(possibleDecisions) == buyHorse:
        buy_pet(pos1x,"horse")
    elif max(possibleDecisions) == buyMosquito:
        buy_pet(pos1x,"mosquito")
    elif max(possibleDecisions) == buyPig:
        buy_pet(pos1x,"pig")
    elif max(possibleDecisions) == buyOtter:
        buy_pet(pos1x,"otter")
    elif max(possibleDecisions) == buyCricket:
        buy_pet(pos1x,"cricket")
    #Items currently broken because of item particles
    #elif max(possibleDecisions) == buyItems:
    #    buyItem()
    elif max(possibleDecisions) == endTurn:
        end_turn()
    elif max(possibleDecisions) == upgradePet:
        upgradeTeamPet()
    elif max(possibleDecisions) == buyRandomPet:
        buy_pet(pos1x,"any")


def main():
    pyautogui.FAILSAFE = True
    start_countdown()
    
    while pyautogui.locateCenterOnScreen("gameover.png") == None:
        chooseNextAction()
    
    
    
if __name__ == "__main__":
    main()

