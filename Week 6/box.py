class Box():
    #Count variable for list
    count = 0
    #Default box constructor
    def __init__(self, bag = [], name = "DEFAULT NAME", description = "DEFAULT DESCRIPTION", owner = "ADMIN"):
        self.bag = bag
        self.name = name
        self.description = description
        self.owner = owner
        
    #Choice print function
    def printValues(self, choice):
        if(choice == "1"):
            #Prints in the format 1.    Cat
            count = 1
            for a in self.bag:
                print(str(count) + ". " + a)
                count = count + 1
        elif(choice == "0"):
            #Prints in the format 0.    Cat
            count = 0
            for a in self.bag:
                print(str(count) + ". " + a)
                count = count + 1
        else:
            #Prints in the format Cat
            for a in self.bag:
                print(a)
              
    #Prints out all formats  
    def fullPrint(self):
        count = 0
        for a in self.bag:
            print(a + "\t" + str(count) + ". " + a + "\t" + str(count + 1) + ". " + a)
            count = count + 1
         
    #Adds item onto list   
    def addItem(self, item):
        self.bag.append(item)
        
    #Prints length of list
    def printLength(self):
        counter = 0
        for a in self.bag:
            counter = counter + 1
        
        return counter
    
    #Prints description of list
    def printDesc(self):
        return self.description
    
    #changes owner of box
    def changeOwner(self, newOwner):
        self.owner = newOwner
      
    #Prints info  
    def printInfo(self):
        print("Bag List: " + str(self.bag))
        print("Name: " + self.name)
        print("Description: " + self.description)
        print("Owner: " + self.owner)