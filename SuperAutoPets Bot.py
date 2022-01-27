
from tabnanny import check
import pyautogui
import time
import random
import cv2


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.5

#shop/team vertical coordinates
teamy = 445
shopy = 715
#Y coordinates to check if pets are empty
#horizontal coordinates for play
pos1x = 555
pos2x = 690
pos3x = 825
pos4x = 960
pos5x = 1095
#items
pos6x = 1230
pos7x = 1365


#Endturn Coordinates
END_TURN_X = 1623
END_TURN_Y = 943

Gold = 10
Turn = 1

#Team Array
Team = [pos1x,pos2x,pos3x,pos4x,pos5x]

#TierList
TierList = ["fish","ant","beaver","mosquito","cricket","otter","horse","pig","duck"]


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
    pyautogui.click(position,teamy)
    global Gold
    Gold -= 3

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
    pyautogui.click()
    time.sleep(15)

#Buys a completely random team
def buyRandomTeam():
    global Turn
    i = 0
    if Turn < 5:
        while (i < 3):
            selection = random.randint(1,3)
            if selection == 1:
                if (check_Slot_Empty(pos1x,shopy) != True):
                    buy_pet(pos1x)
                    print("Pet Purchased!")
                    i += 1
                else: print("No pet available")
            elif selection == 2:
                if (check_Slot_Empty(pos2x,shopy) != True):
                    buy_pet(pos2x)
                    print("Pet Purchased!")
                    i += 1
                else: print("No pet available")
            elif selection == 3:
                if (check_Slot_Empty(pos3x,shopy) != True):
                    buy_pet(pos3x)
                    print("Pet Purchased!")
                    i += 1
                else: print("No pet available")
    elif Turn < 9:
        for x in range(3):
            selection = random.randint(1,5)
            if selection == 1:
                buy_pet(pos1x)
            elif selection == 2:
                buy_pet(pos2x)
            elif selection == 3:
                buy_pet(pos3x)
            elif selection == 4:
                buy_pet(pos4x)
            else:
                buy_pet(pos5x)

#Buy best available pets buy tier
def buyTeamByTier():
    global Gold
    global Team
    if check_Slot_Empty(pos5x,teamy) == True:
        for pet in TierList: 
            buy_pet(pos5x, pet)
            print("Finished checking Slot 1 for ", pet)
    if check_Slot_Empty(pos4x,teamy) == True:
        for pet in TierList: 
            buy_pet(pos4x, pet)
            print("Finished checking Slot 2 for ", pet)
    if check_Slot_Empty(pos3x,teamy) == True:
        for pet in TierList: 
            buy_pet(pos3x, pet)
            print("Finished checking Slot 3 for ", pet)
    if check_Slot_Empty(pos2x,teamy) == True:
        for pet in TierList: 
            buy_pet(pos2x, pet)
            print("Finished checking Slot 4 for ", pet)
    if check_Slot_Empty(pos1x,teamy) == True:
        for pet in TierList: 
            buy_pet(pos1x, pet)
            print("Finished checking Slot 5 for ", pet)

    findGold()
    buyItem()




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
    if pyautogui.locateOnScreen("empty.png", region=(x-70,y-39,135,92,)) != None or pyautogui.pixelMatchesColor(x, y-30, (186, 178, 145))  == True:
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
            pyautogui.click(pos7x,shopy)
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


#Looks for a specific pet in the shop
def findPetShop(pet,shopOrTeam):
    if shopOrTeam == "shop":
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(pet + ".png", confidence=.40, region=(450,600, 1000,200)))
    else: pyautogui.moveTo(pyautogui.locateCenterOnScreen(pet + ".png", confidence=.40, region=(450,320, 1000,200)))


def main():
    pyautogui.FAILSAFE = True
    start_countdown()
    while (pyautogui.locateOnScreen("gameover.png") == None):
        #buyRandomTeam()
        #findGold()
        #buyItem()
        #roll()
        buyTeamByTier()
        end_turn()
        checkWin()
    
    
   
    
    


    
    


if __name__ == "__main__":
    main()

