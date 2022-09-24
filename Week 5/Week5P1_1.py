# Create an animal object with the following characteristics
# Name property
# Species property
# Age property
# Method to display name property
# Method to display species property
# Then create an instance of the object, setting the name, species and age.  Use one of the display properties.
# In the same program, create a second object and use the other display method.

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def printName(self):
        print("Name is: " + self.name)
    
    def printSpecies(self):
        print("Species is: " + self.species)

a1 = Animal("Panda", "Bear", 10)
a1.printName()
a1.printSpecies()

a2 = Animal("Black Bear", "bear", 20)
a2.printName()
a2.printSpecies()
