
#Asks the user for their name
name = raw_input("Enter your name\n")

#Prints the name entered
print("Hello " + name)

#Initialised list and item variable
items = []
item = ""

#While loop to ask for user to enter in item, stops when user enters STOP
while(item != "STOP"):
    item = raw_input("Enter in the name of the item. Type STOP to stop entering\n")

    #Determines whether or not the entered item is STOP. If it is not, then it adds to the list
    #if it is, then the loop stops
    if(item != "STOP"):
        items.append(item)

#Prints out item entered with number
for a in range(len(items)):
    print("Item #" + str(a+1) + ": " + items[a].upper())
