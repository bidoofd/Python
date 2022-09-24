# Global variables

dictionary = {

}

choice = ""

while(choice != "N"):
    # Local variables for the program
    placeList = []
    place = ""
    count = 0

    # Asks user to enter first name and camel case's it
    name = raw_input("What is your first name?\n")
    name.title()

    # Asks the user to enter places. Stops through user input or count
    print("Enter up to 10 places you have been to, or type STOP to stop.")
    while(count != 10 and place != "STOP"):

        # Counter adds 1 to stop loop and user can input
        count = count + 1
        place = raw_input()

        # If the user enters anything other than STOP then it will be added to the list
        if(place != "STOP"):
            placeList.append(place)
    
    # Adds the list to the key in the dictionary
    dictionary[name] = placeList

    # Asks the user whether or not they want to enter another name and capitalises it
    choice = raw_input("Do you want to enter another name? (Y/N)")
    choice.upper()

# Reset counter back to 1 for print
count = 1

# For loop to go through dictionary
for key, value in dictionary.items():

    # Prints the key (name)
    print(key)

    # Goes through the value (list) in the in the key
    for v in value:

        # Prints out list with count adding 1 and the values in the list
        print("\t" + str(count) + ". " + v)
        count = count + 1

    # Resets the counter back to 1 if another name is present
    count = 1
    
        

