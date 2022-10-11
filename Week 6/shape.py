class Shape():
    #Default constructor for shape
    def __init__(self, type= "POLYGON" , sides = 4, colour = "CLEAR", outline = 2):
        self.type = type
        self.sides = sides
        self.colour = colour
        self.outline = outline
        
    #Increases the outline
    def incOutline(self):
        self.outline = self.outline + 1
    
    #Changes the colour
    def changeColour(self, vColour):
        self.colour = vColour
        
    #Prints type
    def seeType(self):
        return self.type
    
    #Prints sides
    def seeSides(self):
        return self.sides
    
    #Prints colour
    def seeColour(self):
        return self.colour
    
    #Prints outline
    def seeOutline(self):
        return self.outline
    
    #prints info of shape
    def printInfo(self):
        print("Type: " + self.type)
        print("Sides: " + str(self.sides))
        print("Colour: " + self.colour)
        print("Outline: " + str(self.outline))
        