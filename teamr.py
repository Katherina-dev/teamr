from random import *
import time
roomNumbers = [0,1,2,3,100,200,101,201,103,104,105,203,204,302,303.402,403]
itemArray = [] 


for i in range(999):
    roomArray.append(False)
    itemArray.append(False)



roomArray[0] = "You find yourself in the basement of house on a chair. There is a loose nail in the chair. There are walls to the North and West of you. To the East there is a rug, and to the South there are stairs." 
roomArray[1] = "To the South is the stairs. To the east there is something in a frame, but you don't know what it is."
roomArray[100] = "You are standing on a very damp rug. There is a weird bump on the rug, it looks suspicious."
roomArray[200] = "To the north and east there is a wall. To the south you see a something in a frame."
roomArray[101] = "To the north of you there is a moist rug. To the east of you there is something that looks like a paper in a picture frame."
roomArray[201] = "There is a wall to the east and south of you. In the corner you see a high school diploma in the picture frame."

itemArray[0] = "Nail"
itemArray[100] = "Watch"
itemArray[201] = "High School Diploma"
itemArray[103] = "books"
itemArray[204] = "pillows"

def doesRoomExist(roomNumber):
    try:
        if roomArray[roomNumber] == False:
            print("You can't go there!")
            return False
        else:
            return True
    except:
        print("You can't go there!")
        return False

def move(userInput, location):
    userInput = userInput.lower()
    if userInput == "n" and roomDoesExist(location - 1):
        location -= 1
    if userInput == "e" and roomDoesExist(location - 1):
        location += 100
    if userInput == "s" and roomDoesExist(location - 1):
        location += 1
    if userInput == "w" and roomDoesExist(location - 1):
        location -= 100
    else:
        print("Invalid option!")
    return location

def main():
  location = 0
  print("The Escape")
  print("By Dhruv, Katherina, Rishil, and Buk")
  time.sleep(1)
  while True:
    print("==========")
    print("Please type n, s, e, w, or quit")
    print("==========")
    userInput = input()
    userInput = userInput.lower()
    if userInput == "quit":
        break
    else:
        location = move(userInput, location)

