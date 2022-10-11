from box import Box
from shape import Shape

#Initialised Variables
item = ""
choice = ""

#Creating shape and incrementing outline
shape1 = Shape()
shape1.printInfo()
shape1.incOutline()
#Prints out incremented outline
print("INCREMENTING OUTLINE TO: " + str(shape1.seeOutline()))
#Prints info of shape
shape1.printInfo()
#Asks user for colour change input
var = input("What colour do you want to change the shape to?\n")
#Changes colour based on input
shape1.changeColour(var)
#Prints out information of shape using methods
print(shape1.seeType())
print(str(shape1.seeSides()))
print(shape1.seeColour())
print(str(shape1.seeOutline()))


#Creates box and prints info
box1 = Box()
box1.printInfo()
#While loop for user to enter items and adds to the box attribute list
    #can enter stop but has to type STOP to stop the actual loop
    
print("Start entering words for a list. Type STOP to stop.")
while(item != "STOP"):
    item = input()
    if(item != "STOP"):
        box1.addItem(item)

#Prints out information of box
print("Length of box: " + str(box1.printLength()))
print("Description of box: " + box1.printDesc())
box1.printInfo()

#Asks user for choice based on what outpet they want to print
print("What do you want to print?")
print("1. Print Start Num 1")
print("0. Print Start Num 0")
choice  = input()
box1.printValues(choice)

#Prints out all cases of outputs
print("FULL PRINT")
box1.fullPrint()

